#!/usr/bin/env bash
set -o errexit

LOCALIP=$1
UZERP_SOURCE_DIR=$2
XDEBUG_CONFIG="remote_host=${LOCALIP} remote_port=9000 remote_log=/var/xdebug.log"
POSTGRES_PASSWORD=xxx
APPARMOR_OPT=""

if [ -d "/sys/kernel/security/apparmor" ]; then
    APPARMOR_OPT="--security-opt apparmor=unconfined"
fi

podman pod create --name uzerp-pod -p 5432 -p 9187 -p 8080:80 -p 8085:5000
podman run --pod uzerp-pod --name uzerp-postgres -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD -d quay.io/uzerp/uzerp-postgres
podman run --pod uzerp-pod --name uzerp-memcache -d memcached

podman run --pod uzerp-pod --name uzerp-app-dev --security-opt label=disable $APPARMOR_OPT \
-v $UZERP_SOURCE_DIR:/var/www/html:rw \
--env XDEBUG_CONFIG="${XDEBUG_CONFIG}" \
-d quay.io/uzerp/uzerp-app-dev

podman run --pod uzerp-pod --name uzerp-frepple --security-opt label=disable $APPARMOR_OPT \
-v ${XDG_CONFIG_HOME:-$HOME/.config}/uzerp/frepple/logs:/app/frepple/logs:rw \
-v ${XDG_CONFIG_HOME:-$HOME/.config}/uzerp/frepple/etc:/etc/frepple:ro \
-d quay.io/uzerp/uzerp-frepple

