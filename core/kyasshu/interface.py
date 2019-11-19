from abc import ABC, abstractmethod


class CacheInterface(ABC):
    """Base Interface of Kyasshu.

    It defines all essential methods needed for a cache.
    """

    @abstractmethod
    def fetch(self, key):
        """Retrives a value for a given key.

        Args:
            key (str): the key to look for.

        Returns:
            The value if a key exists, None otherwise

            The value should have the type that it had when saving.
            Dicts should be fetched as dicts,
            strings as strings, numbers as number, etc.
        """
        pass

    @abstractmethod
    def contains(self, key):
        """Checks if a key exists in the cache.

        Args:
            key (str): the key to look for.

        Returns:
            True if found, False otherwise
        """
        pass

    @abstractmethod
    def save(self, key, data, lifetime=None):
        """Saves a new value to the cache

        Args:
            key (str): The new key to create.
            data (str, int, bool, dict): The value to save.
            lifetime (int, optional): How long should the value be kept?

        Returns:
            True if successful, False otherwise.

        """
        pass

    @abstractmethod
    def delete(self, key):
        """Deletes a key from the cache.

        Args:
            key (str): the key to delete.

        Returns:
            True if successful, False otherwise
        """
        pass


class CacheBackend(CacheInterface):
    """Abstract base class for CacheBackends.

    It extends the CacheInterface and alters it minimally.

    It's mainly used to differentiate backends from Kyasshu's Cache class.

    Additionally it's very cute. :3
    """

    @abstractmethod
    def save(self, key, data, lifetime):
        """
        Additionally:
            A CacheBackend should not accept the lifetime as optinal
            and handle the case of it being None.
        """
        pass
