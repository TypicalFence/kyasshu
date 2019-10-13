from kyasshu import Cache, MemoryBackend

test_dict = {"bunny": "pyon", "cat": "nyan"}
test_binary = bytes([1, 2, 3])
test_number = 42
test_string = "lol"


def get_cache():
    cache = Cache(MemoryBackend())
    cache.save("pyon", test_dict)
    cache.save("bin", test_binary)
    cache.save("num", test_number)
    cache.save("str", test_string)
    return cache


def test_fetch_dict():
    cache = get_cache()
    assert cache.fetch("pyon") == test_dict


def test_fetch_binary():
    cache = get_cache()
    assert cache.fetch("bin") == test_binary


def test_fetch_number():
    cache = get_cache()
    assert cache.fetch("num") == test_number


def test_fetch_string():
    cache = get_cache()
    assert cache.fetch("str") == test_string


def test_fetch_404():
    cache = get_cache()
    assert cache.fetch("404") is None
