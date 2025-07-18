#!/usr/bin/env bash
if [ "$( podman exec -i uzerp-postgres psql -U postgres -tAc "SELECT 1 FROM pg_database WHERE datname='uzerp'" )" = '1' ]
then
    >&2 echo "Database already exists"
else
    podman exec -i uzerp-postgres psql -U postgres -c "create user \"www-data\"  with encrypted password 'xxx';"
    podman exec -i uzerp-postgres psql -U postgres -c "create user sysadmin  with encrypted password 'sysadmin';"
    podman exec -i uzerp-postgres psql -U postgres -c "ALTER USER sysadmin WITH SUPERUSER;"
    podman exec -i uzerp-postgres psql -U postgres -c "create user \"ooo-data\"  with encrypted password 'data123';"
    podman exec -i uzerp-postgres psql -U postgres -c "create user readonly  with encrypted password 'data123';"

    # Create demo database
    podman exec -i uzerp-postgres psql -U postgres -c 'create database uzerp;'
    podman exec -i uzerp-postgres pg_restore -U postgres --dbname=uzerp < $1/schema/database/postgresql/uzerp-demo-dist.sql
