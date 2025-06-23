import os
from pathlib import Path
import shutil
import subprocess
import time
from termcolor import cprint
from xdg import XDG_CONFIG_HOME
from xdg import XDG_DATA_HOME

class Pod(object):
    """
    Podman Pod
    """
    def __init__(self):
        self.update()

    def update(self, pod_name='uzerp-pod', uzerp_file=Path(os.path.join(os.getcwd(), "phinx.yml"))):
        """Update the status of the pod"""
        pod = subprocess.run(["podman", "pod", "ps", '--format="{{.Name}}/{{.ID}}/{{.Status}}"', "--filter=name={}".format(pod_name)], capture_output=True)
        podinfo = pod.stdout.decode("utf-8").replace('"', '').replace('\n', '').split('/')
        self._name = None
        self._id = None
        self._status = None
        self.uzerp_file = uzerp_file
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

        Path(os.path.join(XDG_DATA_HOME, "uzerp", "postgres", "data")).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(XDG_CONFIG_HOME, "uzerp", "postgres")).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(os.path.join(script_dir, "postgres.conf"), os.path.join(XDG_CONFIG_HOME, "uzerp", "postgres", "postgres.conf"))

        if not self.uzerp_file.is_file():
            cprint("Provisioning needed: please run this command in the top-level directory of uzERP source code", 'red')
            exit(1)
        cprint('Creating containers/volumes and adding to pod...', 'green')
        subprocess.run([os.path.join(script_dir, "build-pod.sh"), ip, working_dir], cwd=script_dir)
        cprint('\nBootstrapping postgres databases...', 'green')
        time.sleep(5)
        subprocess.run([os.path.join(script_dir, "pg-bootstrap.sh"), working_dir], cwd=script_dir, stdout=subprocess.DEVNULL)
        cprint('\nuzERP pod ready at http://localhost:8080', 'green')
        
    def xdebugip(self, ip):
        """
        Change the Xdebug remote IP address

        Remove the uzERP app container an recreate it with a new Xdebug configuration.

        It is assumed that the current working directory contains
        the uzERP source code that will be bind mounted to the container.
        """
        if not self.uzerp_file.is_file():
            cprint("Provisioning needed: please run this command in the top-level directory of uzERP source code", 'red')
            exit(1)
        find_app_container = subprocess.run(["podman", "ps", '--filter', 'name=uzerp-app-dev', '--format="{{.ID}}"'], capture_output=True)
        app_container = find_app_container.stdout.decode("utf-8").replace('"', '').replace('\n', '')
        cprint('Replacing app container...', 'green')
        add_container = subprocess.run(["podman", "run", "--replace", "--pod", self._name,
                                        "--name", "uzerp-app-dev",
                                        "--security-opt", "label=disable",
                                        "-v", "{}:/var/www/html:rw".format(os.getcwd()),
                                        "--env", 'XDEBUG_CONFIG=client_host={} client_port=9000 log=/tmp/xdebug.log'.format(ip),
                                        "--env", "XDEBUG_MODE=debug",
                                        "--env", "TZ=Europe/London",
                                        '-d', 'ghcr.io/uzerpllp/uzerp-app-dev'], capture_output=True)

    def up(self, ip):
        """
        Start the pod
        """
        if self._name is None:
            self.provision(ip)
        elif self._name and (self._status == "Stopped" or self._status == "Exited" or self._status == "Created"):
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
