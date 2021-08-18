class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # brute-force solution - TLE
#         closest = -2**32
#         num_len = len(nums)
        
#         for i in range(num_len):
#             for j in range(i + 1, num_len):
#                 for q in range(j + 1, num_len):
#                     three_sum = nums[i] + nums[j] + nums[q]
#                     if abs(three_sum - target) <= abs(closest - target):
#                         closest = three_sum
#         return closest
    
        nums.sort()
        curr_closest = float("inf")
        closest = 0
    
        def twoSumClosest(i: int, l: int) -> int:
            r = len(nums) - 1
            closest = float("inf")
            
            while l < r:
                sum_ = nums[i] + nums[l] + nums[r]
                if sum_ < target:
                    l += 1
                else:
                    r -= 1
                    
                if abs(sum_ - target) < abs(closest - target):
                    closest = sum_
            return closest
        
        for i in range(len(nums) - 1):
            closest = twoSumClosest(i, i + 1)
            curr_closest = closest if abs(closest - target) < abs(curr_closest - target) else curr_closest
        return curr_closest