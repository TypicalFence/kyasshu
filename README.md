# キャッシュ

Kyasshu is a tiny caching library with a simple and minimal interface.

It is inspired by the Cache interface of Doctrine:
https://www.doctrine-project.org/projects/cache.html

I am very bad with comming up with names...

## usage

```python
import time
from kyasshu import Cache, MemoryBackend

cache = Cache(MemoryBackend())
cache.save("my cool data", "very cool data")
cache.save("timed", "my disappearing data", 5)
cool = cache.fetch("my cool data")
print(cool)

cache.delete("my cool data")
uncool = cache.fetch("my cool data")
print(uncool)


print(cache.fetch("timed"))
time.sleep(5)
print(cache.fetch("timed"))
```
