#!/bin/sh

set -e
envsubst '$$EXAMPLE01_VIRTUALHOST' < /etc/nginx/templates/default.conf > /etc/nginx/conf.d/default.conf
envsubst '$$EXAMPLE01_VIRTUALHOST' < /etc/nginx/templates/example01.virtualhost.conf > /etc/nginx/conf.d/example01.virtualhost.conf

# nginx -g 'daemon off;'
