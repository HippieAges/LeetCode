class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, 0
        
        # get the entire nums sum to use in right_sum
        right_sum = sum(nums)
        
        # now we increment the left_sum and decrease
        # the right_sum with each iteration
        for idx in range(len(nums)):
            right_sum -= nums[idx]
            
            if left_sum == right_sum:
                return idx
            left_sum += nums[idx]

        return -1