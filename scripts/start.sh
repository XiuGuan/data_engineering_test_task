#!/usr/bin/env sh
#
# Builds and starts the local postgres data container.

HASH=$(docker build -q .)
PASSWORD=password

docker run \
  --rm \
  -e POSTGRES_PASSWORD=$PASSWORD \
  -p 5432:5432 \
  $HASH