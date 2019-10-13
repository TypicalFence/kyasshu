from .interface import CacheBackend


class DummyBackend(CacheBackend):

    def fetch(self, id):
        return None

    def contains(self, id):
        return False

    def save(self, id, data, lifetime):
        pass

    def delete(self, id):
        pass
