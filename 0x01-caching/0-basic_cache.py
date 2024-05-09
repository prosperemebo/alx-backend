#!/usr/bin/env python3
""" module with implementation for BasicCache class"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    Basic caching system that inherits from BaseCaching.
    """

    def __init__(self):
        """Initialize cache instance"""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache."""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache."""
        return self.cache_data.get(key, None)
