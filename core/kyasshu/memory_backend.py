from datetime import datetime, timedelta
from .interface import CacheBackend


class StoreEntry:

    def __init__(self, data, lifetime=None):
        self._data = data
        self._lifetime = lifetime

    @property
    def data(self):
        return self._data

    @property
    def lifetime(self):
        return self._lifetime


class MemoryBackend(CacheBackend):

    def __init__(self):
        self._store = {}

    def fetch(self, id):
        entry = self._store.get(id)

        if entry is not None:
            if entry.lifetime is None or entry.lifetime > datetime.now():
                return entry.data

        return None

    def contains(self, id):
        return id in self._store

    def save(self, id, data, lifetime):
        now = datetime.now()

        if lifetime is not None:
            now += timedelta(seconds=lifetime)
        else:
            now = None

        self._store[id] = StoreEntry(data, now)

    def delete(self, id):
        try:
            self._store.pop(id)
            return True
        except KeyError:
            return False
