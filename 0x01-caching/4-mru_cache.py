#!/usr/bin/env python3
""" module with implementation of MRUCache class """

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system that inherits from BaseCaching"""

    def __init__(self):
        """Initialize cache instance"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item to the cache."""
        if key and item:
            if self.get(key) != item:
                self.cache_data[key] = item
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    self.cache_data.pop(self.keys[-1])
                    print("DISCARD:", self.keys[-1])
                    self.keys.pop(-1)
                if key not in self.keys:
                    self.keys.append(key)

    def get(self, key):
        """Retrieves an item from the cache."""
        value = self.cache_data.get(key, None)
        if value:
            self.keys.remove(key)
            self.keys.append(key)
        return value
