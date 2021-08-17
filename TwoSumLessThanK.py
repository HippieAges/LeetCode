class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # brute-force solution - O(n^2) time and O(1) space
    
        # max_sum = -1
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (two_sum := nums[i] + nums[j]) < k:
        #             max_sum = max(max_sum, two_sum)
        # return max_sum
        
        # optimized solution - O(nlogn) time and O(1) space
        # I came up with the solution on my own, although I previously
        # had an if for sum_ > k where I also did r -= 1 as in the else
        nums.sort()
        max_sum = -1
        sum_ = 0
        l, r = 0, len(nums) - 1
        
        while l < r:
            sum_ = nums[l] + nums[r]
            if sum_ < k:
                max_sum = max(max_sum, sum_)
                l += 1
            else: # sum_ == k or sum_ > k
                r -= 1
        
        return max_sum