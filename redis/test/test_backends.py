from kyasshu.test import BackendTest
from kyasshu_redis import RedisCache
import fakeredis


class RedisBackendTest(BackendTest):
    __test__ = True

    def get_backend(self):
        return RedisCache(fakeredis.FakeRedis())
