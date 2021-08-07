class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_indices = {0 : -1}
        max_len = 0
        curr_sum = 0
        
        for curr_idx, num in enumerate(nums):
            curr_sum += num
            if (start_idx := sum_indices.get(curr_sum - k, None)) != None:
                max_len = max(max_len, curr_idx - start_idx)
            sum_indices[curr_sum] = sum_indices.get(curr_sum, curr_idx)
        
        return max_len