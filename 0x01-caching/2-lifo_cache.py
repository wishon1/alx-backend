#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from BaseCaching and is a caching
system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent
init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the last item put in cache (LIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Input a new item into the cache"""
        if key is not None or item is not None:
            if key in self.cache_data:
                # Remove the key if it already exists to update its
                # position
                del self.cache_data[key]
            elif len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                # Remove the last item if the cache is full
                lastKey, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {lastKey}")

            # Add the new key-value pair to the cache
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
