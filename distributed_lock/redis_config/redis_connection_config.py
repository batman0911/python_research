import redis

from common.Singleton import Singleton


class RedisConf(metaclass=Singleton):
    __connection = None

    def __init__(self):
        pool = redis.ConnectionPool(host='localhost', port=6379)
        self.__connection = redis.Redis(connection_pool=pool)

    def get_connection(self):
        return self.__connection


if __name__ == '__main__':
    r = RedisConf().get_connection()
    name = r.get("name")
    print(f"my name {name}")


