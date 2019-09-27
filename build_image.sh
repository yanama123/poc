#!/bin/bash

docker pull mysql:8.0
docker pull rabbitmq:3-management

sudo docker build --network="dock_default" -t workerabc .
sudo docker run -d  --network="dock_default" --name working workerabc

virtualenv tas_venv -p python3.6 --never-download
source tas_venv/bin/activate
pip install -r requirements.txt

python3 worker.py > /dev/null &

