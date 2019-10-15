import json
from kyasshu import CacheBackend

def isOneOf(value, types):
    if len(types) == 0:
        return False
    
    current_type = types.pop()
    
    if type(value) is current_type:
        return True
    else:
        return isOneOf(value, types)


class RedisCache(CacheBackend):

    def __init__(self, redis_client):
        self._redis = redis_client
        # self._redis = redis.Redis()

    def fetch(self, id):
        data = self._redis.get(id)

        if data is not None:
            try:
                # try to decode json
                json_str = data.decode("utf8")
                json_data = json.loads(json_str)
                return json_data

            except Exception:
                # return raw value
                return data
                
    def contains(self, id):
        return self._redis.exists(id) > 0

    def save(self, id, data, lifetime):
        # encode value as json becuase redis can only store byte-strings
        # also dicts can't be stored otherwhise
        if isOneOf(data, [dict, str, int, bool, None]):
            data = json.dumps(data)

        return self._redis.set(id, data, lifetime)

    def delete(self, id):
        return self._redis.delete(id) > 1
