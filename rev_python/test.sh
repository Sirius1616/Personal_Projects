#!/usr/bin/bash


cp /etc/hosts ~/etc/host.new

echo "127.0.0.2    localhost" > ~/etc/host.new
echo "8.8.8.8    facebook" >> ~/etc/host.new

cp ~/etc/host.new /etc/host
