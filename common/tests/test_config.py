import unittest
from common import config
from mock import patch


class TestFunction(unittest.TestCase):

    @patch('common.config.file_open')
    def test_get_config(self, file_open_mock):

        # Valid request.
        file_open_mock.return_value = {"rabbitmq": {"RABBIT_MQ_IP": "name"}}
        result = config.get_config("rabbitmq", "RABBIT_MQ_IP")
        self.assertEqual(result, "name")

        # Exception cases.
        with self.assertRaises(KeyError):
            config.get_config("", "")

        file_open_mock.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            config.get_config("rabbitmq", "RABBIT_MQ_IP")