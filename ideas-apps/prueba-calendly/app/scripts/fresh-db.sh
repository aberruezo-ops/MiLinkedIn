#!/bin/sh
# Crea una base limpia con un auth.uid() de desarrollo (en Supabase real ya existe).
D=/tmp/pgdev; P="psql -h $D -p 54330 -U postgres -q -v ON_ERROR_STOP=1"
$P -d postgres -c "drop database if exists clone_test" -c "create database clone_test"
$P -d clone_test -c "create schema auth; create function auth.uid() returns uuid language sql stable as \$\$ select nullif(current_setting('request.jwt.claim.sub', true),'')::uuid \$\$;"
export DATABASE_URL="postgres://postgres@localhost:54330/clone_test?host=$D"
node "$(dirname "$0")/migrate.js" && node "$(dirname "$0")/seed.js"
