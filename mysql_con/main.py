import logging

from logging_research import logging_config

if __name__ == '__main__':
    logging_config.config()
    logger = logging.getLogger()
    logger.info("hello dai ca Linh")