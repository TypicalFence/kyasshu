from .interface import CacheInterface, CacheBackend


class Cache(CacheInterface):
    def __init__(self, backend):
        if not isinstance(backend, CacheBackend):
            raise TypeError()
        self._backend = backend

    def fetch(self, id):
        return self._backend.fetch(id)

    def contains(self, id):
        return self._backend.contains(id)

    def save(self, id, data, lifetime=None):
        return self._backend.save(id, data, lifetime)

    def delete(self, id):
        return self._backend.delete(id)
