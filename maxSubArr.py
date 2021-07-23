class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # technique using Kadane's Algorithm
        local_max = 0
        global_max = -10**5 - 1
        for index in range(len(nums)):
            local_max = max(nums[index], nums[index] + local_max)
            global_max = max(global_max, local_max)
        return global_max