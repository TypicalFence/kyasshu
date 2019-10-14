import pytest
import fakeredis
from kyasshu_redis import RedisCache
from kyasshu.test import BackendTest

class RedisBackendTest(BackendTest):
    __test__ = True

    def get_backend(self):
        return RedisCache(fakeredis.FakeRedis())
