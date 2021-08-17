from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute-force solution - TLE O(n^3)
#         nums.sort()
#         nums_len = len(nums)
#         ans = []
#         triplets = set()
        
#         for i in range(nums_len):
#             for j in range(i + 1, nums_len):
#                 for k in range(j + 1, nums_len):
#                     if nums[i] + nums[j] + nums[k] == 0 and (triplet := (nums[i], nums[j], nums[k])) not in triplets:
#                         ans.append([nums[i], nums[j], nums[k]])
#                         triplets.add(triplet)
                        
#         return ans
        
        # improved brute-force solution - O(n^2) working solution
        nums.sort()
        nums_len = len(nums)
        ans = []
        triplets = set()
        all_nums = set(nums)
        occurrences = Counter(nums)
        
        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                if (num_k := -1 * (nums[i] + nums[j])) in all_nums:
                    
                    if ( (num_k == nums[i] or num_k == nums[j]) and occurrences[num_k] <= 2) or \
                       (num_k, nums[i], nums[j]) in triplets or (nums[i], num_k, nums[j]) in triplets or \
                       (nums[i], nums[j], num_k) in triplets:
                        continue
                    
                    if num_k < nums[i]:
                        ans.append([num_k, nums[i], nums[j]])
                    elif num_k < nums[j]:
                        ans.append([nums[i], num_k, nums[j]])
                    else:
                        ans.append([nums[i], nums[j], num_k])
                    
                    triplets |= {(num_k, nums[i], nums[j]), (nums[i], num_k, nums[j]), (nums[i], nums[j], num_k)}
        return ans