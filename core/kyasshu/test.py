import unittest
from abc import ABC, abstractmethod
from . import Cache, DummyBackend

test_dict = {"bunny": "pyon", "cat": "nyan"}
test_binary = b"\x00\x8a\x00\x00\x00\x00\x00\x00\x05\x00"
test_number = 42
test_string = "lol"


class BackendTest(ABC, unittest.TestCase):

    __test__ = False

    @abstractmethod
    def get_backend(self):
        return DummyBackend()

    def get_cache(self):
        cache = Cache(self.get_backend())
        cache.save("pyon", test_dict)
        cache.save("bin", test_binary)
        cache.save("num", test_number)
        cache.save("str", test_string)
        return cache

    def test_fetch_dict(self):
        cache = self.get_cache()
        assert cache.fetch("pyon") == test_dict

    def test_fetch_binary(self):
        cache = self.get_cache()
        assert cache.fetch("bin") == test_binary

    def test_fetch_number(self):
        cache = self.get_cache()
        assert cache.fetch("num") == test_number

    def test_fetch_string(self):
        cache = self.get_cache()
        assert cache.fetch("str") == test_string

    def test_fetch_404(self):
        cache = self.get_cache()
        assert cache.fetch("404") is None
