# Test Runner
Runner Process to run python/bash test scripts

# Software Requirements
Ubuntu 18.04

Python 3.5

Docker 18.09.7, build 2d0083d

docker-compose 1.24.1, build 4667896b

Rabbitmq 3

Mysql:8

# Python Virtual Environment
Create Python virtual environment

    $ virtualenv test_venv -p python3
Activate virtual environment

    $ source test_venv/bin/activate
Deactivate virtual environment

    $ deactivate
# Project Setup
> To start/enable docker services:
    
    sudo systemctl docker start
    
    sudo systemctl docker-compose start

> Untar project tar at /home directory

    sudo tar -xzvf test_runer-1.0.tar.gz

> Run build_image.sh
  
    sudo ./build_image.sh
   
> Run docker-compose file to run services

    sudo docker-compose up -d 
    
> Run manage.py  to run the test files

    python manage.py -h
    
    python manage.py -tc=test_files/test_python_scripts.py 
    
    python manage.py -tc=test_files/test_shell_scripts.bats
    
> To check test results
>
    python manage.py -a all   
 
    python manage.py -s test_files/test_python_scripts.py
    
    python manage.py -s test_files/test_shell_scripts.bats