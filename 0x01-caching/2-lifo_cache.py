#!/usr/bin/python3
""" lifo cache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add item to cache using LIFO strategy"""
        if key is None or item is None:
            return

        length = len(self.cache_data)
        if key not in self.cache_data and length >= BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop()
            del self.cache_data[last_key]
            print("DISCARD:", last_key)

        if key not in self.cache_data:
            self.stack.append(key)
        else:
            self.stack.remove(key)
            self.stack.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """Retrieve item from cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
