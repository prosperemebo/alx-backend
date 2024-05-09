#!/usr/bin/env python3
""" module with implementation of FIFOCache class """

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system that inherits from BaseCaching """

    def __init__(self):
        """Initialize cache instance"""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache."""
        if key and item and self.get(key) != item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key = next(iter(self.cache_data))
                self.cache_data.pop(key)
                print("DISCARD:", key)

    def get(self, key):
        """Retrieves an item from the cache."""
        return self.cache_data.get(key, None)
