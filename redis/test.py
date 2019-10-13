from redis import Redis
from kyasshu import Cache
from kyasshu_redis import RedisCache

cache = Cache(RedisCache(Redis()))

cache.save("yay", ":3")

print(cache.contains("yay"))
print(cache.fetch("yay"))

d = {"x": "lol", "yay": 21}
cache.save("dict", d)
d2 = cache.fetch("dict")
print(d2)
print(d == d2)
