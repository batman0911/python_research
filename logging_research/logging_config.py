import logging
import datetime

from logging_research.custom_formatter import CustomFormatter
from logging_research.env import Properties


def config():
    conf_property = Properties.get_instance()
    env = conf_property.get_env()
    fmt = env.get("logging_format")

    # Create custom logger logging all five levels
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create stdout handler for logging to the console (logs all five levels)
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(CustomFormatter(fmt))

    # Create file handler for logging to a file (logs all five levels)
    today = datetime.date.today()
    file_handler = logging.FileHandler('logs/my_app_{}.log'.format(today.strftime('%Y_%m_%d')))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(fmt))

    # Add both handlers to the logger
    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)

