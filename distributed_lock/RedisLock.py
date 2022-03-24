from abc import ABC, abstractmethod

from common.Singleton import Singleton
from distributed_lock.redis_config.redis_connection_config import RedisConf


class RedisLock(ABC):
    _default_waiting_time = 1000
    _default_release_time = 5000

    @abstractmethod
    def get_lock(self, lock_name: str, waiting_time=_default_waiting_time, release_time=_default_release_time) -> bool:
        pass

    @abstractmethod
    def release_lock(self, lock_name: str) -> None:
        pass


class SingleRedisLock(RedisLock, ABC):
    __conn = RedisConf().get_connection()

    def __init__(self):
        pass

    def get_lock(self,
                 lock_name: str,
                 waiting_time=super()._default_waiting_time,
                 release_time=super()._default_release_time) -> bool:
        pass

    def release_lock(self, lock_name: str) -> None:
        pass
