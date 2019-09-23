#!/usr/bin/env python
import pika
from common .config import get_config
from common.constant import RABBITMQ_KEY, QUEUE_NAME, ROUTING_KEY


def publish_test(testcase):
    broker = get_config(RABBITMQ_KEY, "RABBIT_MQ_IP")
    user = get_config(RABBITMQ_KEY, "RABBIT_MQ_USERNAME")
    password = get_config(RABBITMQ_KEY, "RABBIT_MQ_PASSWORD")
    credentials = pika.PlainCredentials(user, password)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=broker, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)

    channel.basic_publish(exchange='', routing_key=ROUTING_KEY, body=testcase)
    # print(" [x] Sent 'Hello World!'")
    connection.close()