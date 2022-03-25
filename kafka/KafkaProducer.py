from confluent_kafka import Producer

from common.Singleton import Singleton


class KafkaProducer(metaclass=Singleton):
    __producer = Producer({'bootstrap.servers': 'localhost:9092'})

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
    kafka_producer = KafkaProducer()
    for i in range(10):
        msg = f"message {i}"
        kafka_producer.producer().produce("python-kafka", key="my_name", value=msg, callback=delivery_report)

    kafka_producer.producer().flush()
