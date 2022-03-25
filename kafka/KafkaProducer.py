from confluent_kafka import Producer

from common.config_loader import Config
from common.Singleton import Singleton


class KafkaProducer(metaclass=Singleton):
    __producer = Producer({'bootstrap.servers': 'localhost:9092'})

    def __init__(self):
        """load config from app.yml and init kafka producer"""
        conf = Config().conf()
        bootstrap_server = conf.get("kafka").get("bootstrap-servers")
        print(f'start init kafka server: {bootstrap_server}')
        self.__producer = Producer({'bootstrap.servers': bootstrap_server})

    def producer(self):
        return self.__producer


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')


if __name__ == '__main__':
    producer = KafkaProducer().producer()
    for i in range(10):
        msg = f"message {i}"
        producer.produce("python-kafka", key="my_name", value=msg, callback=delivery_report)

    producer.flush()
