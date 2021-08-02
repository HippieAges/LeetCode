from collections import defaultdict, deque
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = defaultdict(deque)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].appendleft((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        for value, timestamp_prev in self.store[key]:
            if timestamp_prev <= timestamp:
                return value
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)