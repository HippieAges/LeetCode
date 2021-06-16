class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        mapVal = self.map.get(key, -1)
        if mapVal != -1:
            newCache = self.cache + [self.cache.pop(self.cache.index(key))]
            self.cache = newCache
            print(self.cache)
        return mapVal

    def put(self, key: int, value: int) -> None:
        if self.map.get(key, None) != None:
            self.map[key] = value
            newCache = self.cache + [self.cache.pop(self.cache.index(key))]
            self.cache = newCache
        elif len(self.cache) < self.capacity:
            self.cache.append(key)
            self.map[key] = value
        else: # otherwise we need to evict the least recently used key and then insert the new k-v pair
            del self.map[self.cache[0]]
            self.cache.pop(0)

            self.map[key] = value
            self.cache.append(key)

lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
print(lRUCache.get(1))   # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))   # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))    # return -1 (not found)
print(lRUCache.get(3))    # return 3
print(lRUCache.get(4))   # return 4

# lRUCache = LRUCache(1)
# lRUCache.put(2, 1)
# print(lRUCache.get(2))