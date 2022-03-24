from confluent_kafka import Producer


class KafkaProducer:
    __producer = Producer({'bootstrap.server': 'localhost:9092'})

    def __init__(self):
        pass
