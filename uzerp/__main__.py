import os
from pathlib import Path
import shutil
import subprocess
import time
import fire
from termcolor import cprint
from xdg import XDG_CONFIG_HOME


class Pod(object):
  """
  Podman Pod
  """
  def __init__(self):
    self.update()

  def update(self, pod_name='uzerp-pod'):
    """Update the status of the pod"""
    pod = subprocess.run(["podman",  "pod",  "ps", '--format="{{.Name}}/{{.ID}}/{{.Status}}"', "--filter=name={}".format(pod_name)], capture_output=True)
    podinfo = pod.stdout.decode("utf-8").replace('"', '').replace('\n', '').split('/')
    self._name = None
    self._id = None
    self._status = None
    if podinfo[0] != "":
      self._name = podinfo[0]
      self._id = podinfo[1]
      self._status = podinfo[2]

  def getstatus(self):
    """Return the current status of the pod"""
    self.update()
    return self._status

  def provision(self, ip):
    """
    Call the pod build script and bootstrap the databases.
    
    The ip argument is the address for Xdebug connections,
    usually this is an address on the local PC.

    It is assumed that the current working directory contains
    the uzERP source code that will be bind mounted to the container.
    """
    script_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "scripts")
    working_dir = os.getcwd()
    uzerp_file = Path(os.path.join(working_dir, "phinx.yml"))

    Path(os.path.join(XDG_CONFIG_HOME, "uzerp", "frepple", "etc")).mkdir(parents=True, exist_ok=True)
    Path(os.path.join(XDG_CONFIG_HOME, "uzerp", "frepple", "logs", "data", "default")).mkdir(parents=True, exist_ok=True)
    shutil.copyfile(os.path.join(script_dir, "djangosettings.py"), os.path.join(XDG_CONFIG_HOME, "uzerp", "frepple", "etc", "djangosettings.py"))

    if not uzerp_file.is_file():
      cprint("Provisioning needed: please run this command in the top-level directory of uzERP source code", 'red')
      exit(1)
    cprint('Creating containers/volumes and adding to pod...', 'green')
    subprocess.run([os.path.join(script_dir, "build-pod.sh"), ip, working_dir], cwd=script_dir)
    cprint('\nBootstrapping postgres databases...', 'green')
    time.sleep(5)
    subprocess.run([os.path.join(script_dir, "pg-bootstrap.sh"), working_dir], cwd=script_dir, stdout=subprocess.DEVNULL)
    cprint('\nuzERP pod ready at http://localhost:8080', 'green')

  def up(self, ip):
    """
    Start the pod
    """
    if self._name is None:
      self.provision(ip)
    elif self._name and self._status == "Exited":
      subprocess.run(["podman", "pod", "start", self._name])
    self.update()

  def stop(self):
    """Stop the pod"""
    if self._status == "Running":
      subprocess.run(["podman", "pod", "stop", self._name])
    self.update()

  def remove(self):
    """Remove the pod"""
    if self._name:
      subprocess.run(["podman", "pod", "rm", self._name, "--force"])
    self.update()


class cli(object):
  """
  uzERP podman pod control.
  """
  def __init__(self):
    self.our_pod = Pod()

  def up(self, ip='127.0.0.1'):
    """
    Start the uzERP container pod

    Starts the pod using podman or creates one, if it doesn't exist.
    After creating the pod the postgres users and databases are created.

    :param ip: a local ip address for Xdebug connections (uses port 9000).
    WARNING: This must be a real IP, localhost will not work.
    """
    self.our_pod.up(ip)    
    print(self.our_pod.getstatus())

  def halt(self):
    """Stop the uzERP container pod."""
    self.stop()

  def stop(self):
    """Stop the uzERP container pod."""
    cprint('Stopping pod...', 'green')
    self.our_pod.stop()
    print(self.our_pod.getstatus())

  def destroy(self):
    """Remove the uzERP container pod."""
    if self.our_pod.getstatus():
      cprint('Removing pod...', 'green')
      self.our_pod.remove()
      print('Done.')

  def status(self):
    """Show the current status of the uzERP pod."""
    print(self.our_pod.getstatus())

  class db(object):
    """Database operations"""
    def migrate(self):
      """Run phinx migrations"""
      subprocess.run(["podman", "exec", "-i",  "uzerp-app-dev", "php", "vendor/bin/phinx", "migrate", "-e", "development"])

    def rollback(self):
      """Roll back phinx migrations"""
      subprocess.run(["podman", "exec", "-i",  "uzerp-app-dev", "php", "vendor/bin/phinx", "rollback", "-e", "development"])

    def newmigration(self, migration_name):
      """Create new phinx migration"""
      subprocess.run(["podman", "exec", "-i",  "uzerp-app-dev", "php", "vendor/bin/phinx", "create", migration_name])

  class composer(object):
    """Composer commands"""
    def install(self):
      """install/update php dependencies"""
      subprocess.run(["podman", "exec", "-i",  "uzerp-app-dev", "composer", "install"])

def main():
  fire.Fire(cli())
  # c = cli()
  # fire.Fire({'up': c.up,
  #   'status': c.status,
  #   'stop': c.stop,
  #   'halt': c.halt,
  #   'destroy': c.destroy})

if __name__ == '__main__':
  main()
