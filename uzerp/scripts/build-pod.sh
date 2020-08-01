#!/usr/bin/env bash
set -o errexit

LOCALIP=$1
UZERP_SOURCE_DIR=$2
XDEBUG_CONFIG="remote_host=${LOCALIP} remote_port=9000 remote_log=/var/xdebug.log"
POSTGRES_PASSWORD=xxx
TZ="Europe/London"

podman pod create --name uzerp-pod -p 5432 -p 9187 -p 8080:80 -p 8085:5000
podman run -d --pod uzerp-pod --name uzerp-postgres --security-opt label=disable \
-v ${XDG_CONFIG_HOME:-$HOME/.config}/uzerp/postgres/postgres.conf:/etc/postgresql/postgresql.conf \
-v ${XDG_DATA_HOME:-$HOME/.local/share}/uzerp/postgres/data:/var/lib/postgresql/data \
-e TZ=$TZ -e PGTZ=$TZ \
-e POSTGRES_PASSWORD=$POSTGRES_PASSWORD quay.io/uzerp/uzerp-postgres \
-c "config_file=/etc/postgresql/postgresql.conf"

podman run --pod uzerp-pod --name uzerp-memcache -e TZ=$TZ -d memcached

podman run --pod uzerp-pod --name uzerp-app-dev --security-opt label=disable \
-v $UZERP_SOURCE_DIR:/var/www/html:rw \
--env XDEBUG_CONFIG="${XDEBUG_CONFIG}" -e TZ=$TZ \
-d quay.io/uzerp/uzerp-app-dev

podman run --pod uzerp-pod --name uzerp-frepple --security-opt label=disable \
-v ${XDG_DATA_HOME:-$HOME/.local/share}/uzerp/frepple/logs:/app/frepple/logs:rw \
-v ${XDG_CONFIG_HOME:-$HOME/.config}/uzerp/frepple/etc:/etc/frepple:ro \
-e TZ=$TZ \
-d quay.io/uzerp/uzerp-frepple

