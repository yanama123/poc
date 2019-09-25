#!/usr/bin/env python
import pika
import os
from utils import utility
from common .config import get_config
from common.constant import RABBITMQ_KEY, QUEUE_NAME
__path__ = [os.path.dirname(os.path.abspath(__file__))]


broker = get_config(RABBITMQ_KEY, "RABBIT_MQ_IP")
user = get_config(RABBITMQ_KEY, "RABBIT_MQ_USERNAME")
password = get_config(RABBITMQ_KEY, "RABBIT_MQ_PASSWORD")
credentials = pika.PlainCredentials(user, password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=broker, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue=QUEUE_NAME)
# channel.basic_qos(prefetch_count=1)
channel.basic_consume(consumer_callback=utility.read_test_case, queue=QUEUE_NAME)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

