import logging
import json

from logging_research.env import Properties


def config():
    conf_property = Properties.get_instance()
    env = conf_property.get_env()

    logging.basicConfig(level=logging.INFO,
                        format=env.get("logging_format"))
