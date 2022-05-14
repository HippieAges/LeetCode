from __future__ import annotations
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1

#   recursive approach: O(logn) time & O(1) space complexity
#         def helper(left: int, right: int) -> int:
#             mid = (left + right) // 2
#             if left > right:
#                 return -1
#             if target < nums[mid]:
#                 return helper(left, mid - 1)
#             elif target > nums[mid]:
#                 return helper(mid + 1, right)
#             return mid
        
#         return helper(left, right)
        # refined approach: O(logn) time & O(1) space complexity 
        def bisect_helper() -> int:
            bisect_val = bisect.bisect_left(nums, target) 
            return -1 if bisect_val >= len(nums) or nums[bisect_val] != target else bisect_val
        
        return bisect_helper()
# iterative approach: O(logn) time & O(1) space complexity
#         index = -1
        
#         while left <= right:
#             mid = (left + right) // 2
            
#             if target < nums[mid]:
#                 right = mid - 1
#             elif target > nums[mid]:
#                 left = mid + 1
#             else:
#                 return mid
#         return index

S = Solution()
print(S.search([-1,0,3,5,9,12], 9))