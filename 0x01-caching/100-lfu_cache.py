from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """LFU Cache System"""

    def __init__(self):
        """Initialize the LFU Cache"""
        super().__init__()
        self.freq_counter = defaultdict(int)
        self.usage_order = []

    def put(self, key, item):
        """Add an item to cache using LFU strategy"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq_counter[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq_counter.values())
                lfu_keys = [
                        k for k in self.cache_data
                        if self.freq_counter[k] == min_freq
                        ]

                for old_key in self.usage_order:
                    if old_key in lfu_keys:
                        discard = old_key
                        break

                del self.cache_data[discard]
                del self.freq_counter[discard]
                self.usage_order.remove(discard)
                print("DISCARD:", discard)

            self.cache_data[key] = item
            self.freq_counter[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """Retrieve item from cache and update usage"""
        if key is None or key not in self.cache_data:
            return None

        self.freq_counter[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
