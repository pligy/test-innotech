#!/bin/sh

envsubst '${DEFAULT_PORT}' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf

exec "$@"
