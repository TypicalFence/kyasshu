import json
from kyasshu import CacheBackend


class RedisCache(CacheBackend):

    def __init__(self, redis_client):
        self._redis = redis_client
        # self._redis = redis.Redis()

    def fetch(self, id):
        data = self._redis.get(id)

        # TODO remove json, use redis hash instead
        if data is not None:
            try:
                json_str = data.decode("utf8")
                json_data = json.loads(json_str)
                return json_data

            except UnicodeDecodeError:
                return data

            except ValueError:
                # FIXME this is very bad
                # maybe we should change the interface
                # this method feels very galaxy brain
                try:
                    str_data = data.decode("utf8")
                    if len(str_data) > 0:
                        return str_data

                except UnicodeDecodeError:
                    return data

            return data

    def contains(self, id):
        return self._redis.exists(id) > 0

    def save(self, id, data, lifetime):
        if type(data) is dict:
            data = json.dumps(data)

        return self._redis.set(id, data, lifetime)

    def delete(self, id):
        return self._redis.delete(id) > 1
