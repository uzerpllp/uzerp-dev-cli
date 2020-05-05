#!/usr/bin/env bash
set -o errexit

LOCALIP=$1
UZERP_SOURCE_DIR=$2
XDEBUG_CONFIG="remote_host=${LOCALIP} remote_port=9000"
POSTGRES_PASSWORD=xxx

podman pod create --name uzerp-pod -p 5432 -p 9187 -p 8080:80 -p 8085:5000
podman run --pod uzerp-pod --name uzerp-postgres -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD -d uzerp-postgres
podman run --pod uzerp-pod --name uzerp-memcache -d memcached

podman run --pod uzerp-pod --name uzerp-app-dev --security-opt label=disable \
-v $UZERP_SOURCE_DIR:/var/www/html:rw \
--env XDEBUG_CONFIG="${XDEBUG_CONFIG}" \
-d uzerp-apache

podman run --pod uzerp-pod --name uzerp-frepple --security-opt label=disable \
-v ${XDG_CONFIG_HOME:-$HOME/.config}/uzerp/frepple/logs:/app/frepple/logs:rw \
-v ${XDG_CONFIG_HOME:-$HOME/.config}/uzerp/frepple/etc:/etc/frepple:ro \
-d uzerp-frepple
