from kyasshu import MemoryBackend
from kyasshu.test import BackendTest


class MemoryBackendTest(BackendTest):
    __test__ = True

    def get_backend(self):
        return MemoryBackend()
