import json
from kyasshu import CacheBackend

# TODO remove json, use redis hash instead


class RedisCache(CacheBackend):

    def __init__(self, redis_client):
        self._redis = redis_client
        # self._redis = redis.Redis()

    def fetch(self, id):
        data = self._redis.get(id)
        if data is not None:
            json_str = data.decode("utf8")
            try:
                json_data = json.loads(json_str)
                return json_data
            except ValueError:
                return data

    def contains(self, id):
        return self._redis.exists(id) > 0

    def save(self, id, data, lifetime):
        if type(data) is dict:
            data = json.dumps(data)

        return self._redis.set(id, data, lifetime)

    def delete(self, id):
        return self._redis.delete(id) > 1
