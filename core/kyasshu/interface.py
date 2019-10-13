from abc import ABC, abstractmethod


class CacheInterface(ABC):

    @abstractmethod
    def fetch(self, id):
        pass

    @abstractmethod
    def contains(self, id):
        pass

    @abstractmethod
    def save(self, id, data, lifetime):
        pass

    @abstractmethod
    def delete(self, id):
        pass


class CacheBackend(CacheInterface):

    @abstractmethod
    def save(self, id, data, lifetime=None):
        pass
