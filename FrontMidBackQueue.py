from collections import deque

# O(n) time complexity for pushMiddle() & popMiddle() due to having to iterate over n / 2 elements to get to mid
# O(1) time complexity for every other method
# O(n) space complexity due to using a deque data structure
class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = deque()

    def pushFront(self, val: int) -> None:
        self.queue.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        queue_mid = len(self.queue) // 2
        self.queue.insert(queue_mid, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if not self.queue:
            return -1
        return self.queue.popleft()
    
    def popMiddle(self) -> int:
        if not self.queue:
            return -1
        queue_mid = len(self.queue) // 2 if not len(self.queue) % 2 == 0 else len(self.queue) // 2 - 1
        mid_elem = self.queue[queue_mid]
        del self.queue[queue_mid]
        return mid_elem

    def popBack(self) -> int:
        if not self.queue:
            return -1
        return self.queue.pop()