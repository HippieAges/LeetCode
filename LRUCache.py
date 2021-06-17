import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.map = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        mapVal = self.map.get(key, -1)
        if mapVal != -1:
            self.map.move_to_end(key, last=False)
        return mapVal

    def put(self, key: int, value: int) -> None:
        if len(self.map) >= self.capacity and self.map.get(key, None) == None:
            self.map.popitem(last=True)
        self.map[key] = value
        self.map.move_to_end(key, last=False)

        

lRUCache = LRUCache(3)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
lRUCache.put(3, 3) # cache is {1=1, 2=2}
lRUCache.put(4, 4) # cache is {1=1, 2=2}
print(lRUCache.get(4))   # return 1
print(lRUCache.get(3))   # return 1
print(lRUCache.get(2))   # return 1
print(lRUCache.get(1))   # return 1
lRUCache.put(5, 5) # cache is {1=1, 2=2}
print(lRUCache.get(1))   # return 1
print(lRUCache.get(2))   # return 1
print(lRUCache.get(3))   # return 1
print(lRUCache.get(4))   # return 1
print(lRUCache.get(5))   # return 1

# lRUCache.put(1, 1) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# # print(lRUCache.get(2))   # returns -1 (not found)
# lRUCache.put(4, 1) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# print(lRUCache.get(2))    # return -1 (not found)
# print(lRUCache.get(3))    # return 3
# print(lRUCache.get(4))   # return 4

# lRUCache = LRUCache(1)
# lRUCache.put(2, 1)
# print(lRUCache.get(2))

# lRUCache = LRUCache(2)
# print(lRUCache.put(1, 1), end=" ")
# print(lRUCache.put(2, 2), end=" ")
# print(lRUCache.get(1), end=" ")
# print(lRUCache.put(3, 3), end=" ")
# print(lRUCache.get(2), end=" ")
# print(lRUCache.put(4, 4), end=" ")
# print(lRUCache.get(1), end=" ")
# print(lRUCache.get(3), end=" ")
# print(lRUCache.get(4))