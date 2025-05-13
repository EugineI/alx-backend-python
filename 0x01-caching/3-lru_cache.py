#!/usr/bin/python3
"""lru cache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Cache system"""

    def __init__(self):
        """Initialize the LRU Cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache with LRU eviction"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve item from cache and mark it as recently used"""
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
