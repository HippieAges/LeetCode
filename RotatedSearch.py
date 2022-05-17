from __future__ import annotations
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute-force solution
        # O(n) where n is the size of nums for time complexity & O(1) space complexity
        # first find the possible pivot index
        pivot_idx = -1
        array_len = len(nums) 
        # for idx in range(array_len):
        #     if idx + 1 < array_len and nums[idx] > nums[idx + 1]:
        #         pivot_idx = idx + 1
        #         break
                
        def perform_search(low: int = 0, high: int = array_len) -> int:
            possible_idx = bisect.bisect_left(nums, target, low, high)
            return -1 if possible_idx >= array_len or nums[possible_idx] != target else possible_idx
        
        # optimized-solution of O(logn) time & O(1) space complexity
        # first find the possible pivet index using binary search
        left, right = 0, array_len - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                right = mid - 1
                pivot_idx = mid # pivot_idx must be mid or less
            elif nums[right] < nums[mid]:
                left = mid + 1 
                pivot_idx = left # pivot_idx must at least be mid + 1 or greater
            else:
                break
        
        # if there is not a pivot index, run binary search once, otherwise we need to run it twice
        if pivot_idx == -1:
            return perform_search()
        else:
            left_sub_idx = perform_search(0, pivot_idx - 1)
            right_sub_idx = perform_search(pivot_idx, array_len)
            return left_sub_idx if right_sub_idx == -1 else right_sub_idx
        