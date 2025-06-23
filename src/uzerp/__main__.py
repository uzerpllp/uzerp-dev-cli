import os
from pathlib import Path
import subprocess
import fire
from termcolor import cprint
from uzerp.pod import Pod

__version__ = "1.2"


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

    def debugip(self, ip):
        """Change the Xdebug remote IP address
        
        :param ip: a local ip address for Xdebug connections (uses port 9000).
        WARNING: This must be a real IP, localhost will not work.
        """
        self.our_pod.xdebugip(ip)

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
        def migrate():
            """Run phinx migrations"""
            subprocess.run(["podman", "exec", "-i", "uzerp-app-dev", "php", "vendor/bin/phinx", "migrate", "-e", "development"])

        def rollback():
            """Roll back phinx migrations"""
            subprocess.run(["podman", "exec", "-i", "uzerp-app-dev", "php", "vendor/bin/phinx", "rollback", "-e", "development"])

        def newmigration(migration_name):
            """Create new phinx migration"""
            subprocess.run(["podman", "exec", "-i", "uzerp-app-dev", "php", "vendor/bin/phinx", "create", migration_name])

    class composer(object):
        """Composer commands"""
        def install():
            """install php dependencies"""
            subprocess.run(["podman", "exec", "-i", "uzerp-app-dev", "composer", "install"])

        def update():
            """update php dependencies"""
            subprocess.run(["podman", "exec", "-i", "uzerp-app-dev", "composer", "update"])

def main():
    c = cli()
    fire.Fire({'up': c.up,
        'debugip': c.debugip,
        'status': c.status,
        'stop': c.stop,
        'halt': c.halt,
        'destroy': c.destroy,
        'db': {
            'migrate': c.db.migrate,
            'rollback': c.db.rollback,
            'newmigration': c.db.newmigration},
        'composer': {
            'install': c.composer.install,
            'update': c.composer.update}
    })

if __name__ == '__main__':
    main()
