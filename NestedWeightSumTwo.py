# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        
        # solution 1 - O(n) time and O(n) space
        # max_depth = self.findMaxDepth(1, 1, nestedList)
        
        # solution 2 - O(n) time (but less code compared to solution 1) and O(n*m) space 
        max_depth, queue = self.new_dfs(1, 1, nestedList)
        nested_sum = 0
        
        for elem, depth in queue:
            nested_sum += elem * (max_depth - depth + 1)
        return nested_sum
        
        return self.dfs(1, max_depth, nestedList)
    
#     def findMaxDepth(self, max_depth: int, curr_depth: int, nestedList: List[NestedInteger]) -> int:
#         for elem in nestedList:
#             if elem.isInteger():
#                 max_depth = max(max_depth, curr_depth)
#             else:
#                 max_depth = max(max_depth, self.findMaxDepth(max_depth, curr_depth + 1, elem.getList()))
#         return max_depth
    
#     def dfs(self, curr_depth: int, max_depth: int, nestedList: List[NestedInteger]) -> int:
#             nestedSum = 0
#             for elem in nestedList:
#                 if elem.isInteger():
#                     nestedSum += elem.getInteger() * (max_depth - curr_depth + 1) 
#                 else:
#                     nestedSum += self.dfs(curr_depth + 1, max_depth, elem.getList())
#             return nestedSum
        
    def new_dfs(self, curr_depth: int, max_depth: int, nestedList: List[NestedInteger]) -> Tuple[int]:
        queue = []
        for elem in nestedList:
            if elem.isInteger():
                queue.append( (elem.getInteger(), curr_depth) )
                max_depth = max(max_depth, curr_depth)
            else:
                depth, elems = self.new_dfs(curr_depth + 1, max_depth, elem.getList())
                queue.extend(elems)
                max_depth = max(depth, max_depth)
        return max_depth, queue