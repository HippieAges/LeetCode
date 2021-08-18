class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # brute-force solution - TLE
        # target_smaller = 0
        # nums_len = len(nums)
        # for i in range(nums_len):
        #     for j in range(i + 1, nums_len):
        #         for k in range(j + 1, nums_len):
        #             if nums[i] + nums[j] + nums[k] < target:
        #                 target_smaller += 1
        # return target_smaller
        
        nums.sort()
        num_triplets = 0
        
        def twoSumsSmaller(l : int, target : int) -> List[int]:        
            sum_ = 0
            two_sums = 0
            r = len(nums) - 1

            while l < r:
                sum_ = nums[l] + nums[r]
                if sum_ < target:
                    two_sums += r - l # LC solution, forgot that everything prior is also included
                    l += 1
                else: # sum_ == target or sum_ > target
                    r -= 1
            return two_sums
            
        for i in range(len(nums) - 1):
            two_sums = twoSumsSmaller(i + 1, target - nums[i])
            print(two_sums)
            num_triplets += two_sums
        return num_triplets