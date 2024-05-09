#!/usr/bin/env python3
""" module with implementation of LRUCache class """

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRUCache caching system that inherits from BaseCaching"""

    def __init__(self):
        """Initialize cache instance"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item to the cache."""
        if key and item:
            if self.get(key) != item:
                self.cache_data[key] = item
                if key not in self.keys:
                    self.keys.append(key)
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    self.cache_data.pop(self.keys[0])
                    print("DISCARD:", self.keys[0])
                    self.keys.pop(0)

    def get(self, key):
        """Retrieves an item from the cache."""
        value = self.cache_data.get(key, None)
        if value:
            self.keys.remove(key)
            self.keys.append(key)
        return value
