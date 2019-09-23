### Software Requirments

    Python 3.6.7

### Clone Repo

    $ git clone https://github.com/yanama123/Python_Automation.git

### Python Virtual Environment

1. Create Python virtual environment

        $ virtualenv test_venv -p python3

2. Activate virtual environment

        $ source test_venv/bin/activate

3. Deactivate virtual environment

        $ deactivate

### RabbitMQ installation

    echo "deb http://www.rabbitmq.com/debian/ testing main"  | sudo tee  /etc/apt/sources.list.d/rabbitmq.list > /dev/null
    wget https://www.rabbitmq.com/rabbitmq-signing-key-public.asc
    sudo apt-key add rabbitmq-signing-key-public.asc
    sudo apt-get update
    sudo apt-get install rabbitmq-server -y
    sudo service rabbitmq-server start
    sudo rabbitmq-plugins enable rabbitmq_management
    sudo service rabbitmq-server restart
