#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent
init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least recently used item (LRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Input a new item into the cache"""
        if key is None and item is None:
            pass
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                # Remove the least recently used item if the cache is full
                first_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {first_key}")

            # Add the new key-value pair to the cache
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the front to mark it as recently used
        self.cache_data.move_to_end(key, last=False)
        return self.cache_data[key]
