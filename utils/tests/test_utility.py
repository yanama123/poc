import unittest
from utils import utility
from mock import patch
from  rabbitmq.tests.mocked_rabbitmq import rabbitmqmockmethods
from rabbitmq.tests.mocked_rabbitmq import channelmock
from rabbitmq.tests.mocked_rabbitmq import method
from mock import MagicMock


class TestUtility(unittest.TestCase):
    @patch('rabbitmq.producer.pika.BlockingConnection')
    @patch('worker.basic_consume')
    def test_read_test_case(self, service_now_mock, blocking_connection_mock ):
        pass