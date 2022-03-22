import logging
import logging_config

log = logging.getLogger(__name__)


def greeting(name):
    log.info(f'hello {name}')


if __name__ == '__main__':
    logging_config.config()
    log = logging.getLogger("main")
    log.info("hello from main")
    greeting('dai ca Linh')


