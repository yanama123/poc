import unittest
from rabbitmq import producer
from rabbitmq.tests.mocked_rabbitmq import rabbitmqmockmethods
from mock import patch


def mock_get_config(key, attribute):
    data_dict = {"rabbitmq": {"RABBIT_MQ_IP": "localhost", "RABBIT_MQ_USERNAME": "mqadmin",
                              "RABBIT_MQ_PASSWORD": "mqadminpassword"}}
    return data_dict[key][attribute]


class TestRabbitmq(unittest.TestCase):

    @patch('rabbitmq.producer.pika.BlockingConnection')
    @patch('common.config.get_config')
    def test_publish_message(self, config_mock, blocking_connection_mock):
        blocking_connection_mock.return_value = rabbitmqmockmethods()
        config_mock.side_effect = mock_get_config
        result = producer.publish_test({"test_python_scripts.py"})
        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.TestCase()