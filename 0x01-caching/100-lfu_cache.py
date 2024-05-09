#!/usr/bin/env python3
""" module with implementation of LFUCache class """

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """LRU caching system that inherits from BaseCaching"""

    def __init__(self):
        """Initialize cache instance"""
        super().__init__()
        self.keys = {}

    def put(self, key, item):
        """Add an item to the cache."""
        if key and item:
            if self.get(key) != item:
                self.cache_data[key] = item
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    k = min(self.keys, key=self.keys.get)
                    self.cache_data.pop(k)
                    print("DISCARD:", k)
                    self.keys.pop(k)
                if key not in self.keys:
                    self.keys[key] = 0

    def get(self, key):
        """Retrieves an item from the cache."""
        value = self.cache_data.get(key, None)
        if value:
            self.keys[key] += 1
        return value
