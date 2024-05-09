#!/usr/bin/env python3
""" module with implementation of LIFOCache class """

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system that inherits from BaseCaching"""

    def __init__(self):
        """Initialize cache instance"""
        super().__init__()
        self.last = None

    def put(self, key, item):
        """Add an item to the cache."""
        if key and item:
            if self.get(key) != item:
                self.cache_data[key] = item
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    self.cache_data.pop(self.last)
                    print("DISCARD:", self.last)
                self.last = key

    def get(self, key):
        """Retrieves an item from the cache."""
        return self.cache_data.get(key, None)
