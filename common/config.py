import os
import logging
import yaml
from os.path import join
from common.constant import CONFIG_FILE_PATH

logger = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def file_open(file_name):
    """

    :param file_name:
    :return:
    """
    with open(file_name, 'r') as f:
        return yaml.load(f)


def get_config(key, attribute):
    """
    sample yaml file
    :param key: yaml root key
    :param attribute: yaml nested key
    :return: value corresponding to the parameter
    """
    logger.info("Inside: get_config")
    logger.debug("get_config: parameters - {}, {}".format(key, attribute))
    try:
        doc = file_open(join(BASE_DIR, CONFIG_FILE_PATH))
        param_value = doc[key][attribute]
        logger.info("Exit: get_config")
        return param_value
    except KeyError as e:
        e.message = "Missing key : {}".format(e)
        logger.exception(e)
        raise
    except FileNotFoundError as e:
        e.message = "{} : {}".format(e.strerror, e.filename)
        logger.exception(e)
        raise
