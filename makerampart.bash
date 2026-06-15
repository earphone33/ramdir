#!/usr/bin/bash

echo "makerampart.bash is now running"

sudo mkdir /tmp/ramdir
sudo mount -t tmpfs -o size=$1 tmpfs /tmp/ramdir
echo "==> tmpfs of size $1 created"

echo "makerampart.bash exites"
