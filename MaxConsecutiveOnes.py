class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        num_ones = 0
        ans = 0
        
        for num in nums:
            if num == 1:
                num_ones += 1
            else:
                num_ones = 0
            ans = max(ans, num_ones)
    
        return ans