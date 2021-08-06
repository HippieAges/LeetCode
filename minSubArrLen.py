import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums) + 1
        r, l = 0, 0
        curr = 0
        
        while r >= l:
            if curr >= target:
                idx_range = 1 if r - l == 0 else r - l
                min_len = min(min_len, idx_range)
                    
            if curr <= target and r < len(nums):
                curr += nums[r]
                r += 1
            elif curr >= target:
                curr -= nums[l]
                l += 1
            elif r >= len(nums):
                l += 1

        return 0 if min_len == len(nums) + 1 else min_len