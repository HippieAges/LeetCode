class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # brute-force solution - time is O(n^2), space is O(1)
        
#         curr_sum = 0
#         ans = 0
#         count = 0
        
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if k > 0 or nums[j] == 1:
#                     curr_sum += 1
#                 if k > 0 and nums[j] == 0:
#                     count += 1
#                 ans = max(ans, curr_sum)
#                 if count == k and j + 1 < len(nums) and nums[j + 1] == 0:
#                     break
#             count = 0
#             curr_sum = 0
            
#         return ans
        
#         left, right = 0, 0
#         # prev_left = 0

        ans = k
        left = 0
        num_zeros = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeros += 1
                        
            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans