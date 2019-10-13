"""キャッシュ

Kyasshu is a tiny caching library with a simple and minimal interface.

It is inspired by the Cache interface of Doctrine:
https://www.doctrine-project.org/projects/cache.html
"""
from .interface import CacheInterface, CacheBackend
from .cache import Cache
from .memory_backend import MemoryBackend
from .dummy_backend import DummyBackend
