#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from BaseCaching and is a caching
system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init:
super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """initialize the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """insert an itenm in the cache memory based on the given key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            firstKey = self.cache_data.popitem(False)
            print(f"DISCARD: {firstKey}")

    def get(self, key):
        """return the value in self.cache_data linked to key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
