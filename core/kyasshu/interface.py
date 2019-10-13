from abc import ABC, abstractmethod


class CacheInterface(ABC):
    """Base Interface of Kyasshu.

    It defines all essential methods needed for cache.
    """

    @abstractmethod
    def fetch(self, id):
        pass

    @abstractmethod
    def contains(self, id):
        pass

    @abstractmethod
    def save(self, id, data, lifetime=None):
        pass

    @abstractmethod
    def delete(self, id):
        pass


class CacheBackend(CacheInterface):
    """Abstract base class for CacheBackends.

    It extends the CacheInterface and alters it minimally.

    It's mainly used to differentiate backends from Kyasshu's Cache class.
    """

    @abstractmethod
    def save(self, id, data, lifetime):
        pass
