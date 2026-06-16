#!/usr/bin/bash

echo "makerampart.bash is now running"

sudo mkdir $2
sudo mount -t tmpfs -o size=$1 tmpfs $2
echo "==> tmpfs of size $1 created at $2"

echo "makerampart.bash exites"
