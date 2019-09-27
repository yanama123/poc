#!/bin/bash
docker pull mysql:8.0

docker pull rabbitmq:3-management

sudo docker build --network="dock_default" -t workerabc .
sudo docker run -d  --network="dock_default" --name working workerabc
