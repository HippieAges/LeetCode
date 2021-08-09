from collections import deque

class MaxQueue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, elem):
        while len(self.queue) and elem[0] > self.queue[-1][0]:
            self.queue.pop()
        self.queue.append(elem)
    
    def pop(self):
        return self.queue.popleft()
    
    
    def getMax(self):
        return self.queue[0][0]
    
    def peekTop(self):
        return self.queue[0][1]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute-force solution
        # two for loops
        # outer for loop goes up to the len(nums) - k element
        # inner for loop goes over the next k - 1 elements to check for the max 
        
#         maxs = []
        
#         index = 0
#         while index <= len(nums) - k:
#             maxs.append(max(nums[index:index + k]))
#             index += 1
        
#         return maxs

        max_sliding_window = []
        queue = MaxQueue()
        
        # add the first k elements to the maxQueue
        for i in range(k):
            queue.push( (nums[i], i) )
        max_sliding_window.append(queue.getMax())
        
        for idx in range(k, len(nums)):
            
            if len(queue.queue) == k or idx - k >= queue.peekTop():
                queue.pop()
            queue.push( (nums[idx], idx) )
            max_sliding_window.append(queue.getMax())
        return max_sliding_window