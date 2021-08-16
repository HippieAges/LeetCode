class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # naive approach - O(nlogn) time and O(1) space
#         nums.sort()
        
#         curr_num = nums[0]
#         missing_num = nums[-1] + 1 if curr_num == 0 else 0
#         for num in nums:
#             if num != curr_num:
#                 missing_num = curr_num
#                 break
#             curr_num += 1
#         return missing_num
    
        # slightly better solution - O(n) time and space
        all_nums = set()
        missing_num = 0
        
        for num in nums:
            all_nums.add(num)
            
        all_nums_len = len(all_nums)
        
        for num in all_nums:
            if (val := num + 1) <= all_nums_len and val not in all_nums:
                missing_num = val
                break
        return missing_num