# uzERP Development CLI

The uzERP development CLI provides an easy way to get a local ERP development or demo environment up and running quickly.

## Features

* Runs uzERP and associated software in containers
* Uses podman to run containers in a pod, where they communicate on localhost
* Provides convenience commands:
    * Set a local IP for Xdebug to connect back to when debugging PHP
    * Create and execute phinx migrations in the uzERP container
    * Run Composer install and update inside the uzERP container

## Installation and Set-up

### Podman

The uzERP dev CLI uses podman to run the required containers. Simply `dnf install podman`.

### uzERP Development Commandline

Before installing this package, install some additional requirements:

* pip, used to install python packages
* git, required to get the uzERP source code
* npm, needed to build uzERP front-end assets

```
$ sudo apt install python3-pip git npm
```

On Ubuntu you might need edit your `.bashrc` file to ensure that the path for user-binaries is set by appending the following:

```
export PATH="$(systemd-path user-binaries):$PATH"
```

Close the terminal session and start a new one, then install the CLI package:

```
$ pip3 install --user https://github.com/uzerpllp/uzerp-dev-cli/dist/uzerp-1.2-py3-none-any.whl
```

### Set-up uzERP

Download the uzERP source:

```
$ cd ~/
$ git clone https://github.com/uzerpllp/uzerp.git
```

Start uzERP. This will create configuration files and data directories, create the container pod and bootstrap the databases.

```
$ cd uzerp
$ uzerp up
```

Install PHP dependencies, build the frontend assets and prepare a uzERP config file.

```
$ uzerp composer install
$ npm install
$ npm run gulp
$ cp conf/config-example.php conf/config.php
```

Edit config.php. Change database name to 'uzerp' and host to 'localhost'.

Set ownership of the data directory that www-data inside the container can create directories/files:

```
podman unshare chown 33:33 -R ./data
```

Browse to http://localhost:8080 and log in to uzERP with the default password username and password admin/admin

## CLI Commands

For help on available commands, use the help facility:


```
$ uzerp --help
```

## Tips and Tricks

See a list of the running containers:

`$ podman ps`

Inspect the postgresql log:

`$ podman log uzerp-postgres`
