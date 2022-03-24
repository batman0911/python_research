import logging
import logging_config


if __name__ == '__main__':
    logging_config.config()
    logger = logging.getLogger()
    # log = logging.getLogger("main")
    # log.info("hello from main")
    # greeting('dai ca Linh')

    logger.debug('This is a debug-level message')
    logger.info('This is an info-level message')
    logger.warning('This is a warning-level message')
    logger.error('This is an error-level message')
    logger.critical('This is a critical-level message')

