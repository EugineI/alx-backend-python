#!/usr/bin/python3
"""fifo"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system """

    def __init__(self):
        """ Initialize the FIFO cache """
        super().__init__()
        self.order = []  # To keep track of insertion order

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm """
        if key is None or item is None:
            return

        length = len(self.cache_data)
        if key not in self.cache_data and length >= BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print("DISCARD:", oldest_key)

        if key not in self.cache_data:
            self.order.append(key)
        # Add or update the key
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
