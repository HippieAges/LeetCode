class Solution:
    def minSwaps(self, data: List[int]) -> int:
        num_swaps = 0
        min_swaps = 10**5
        left = 0
        
        num_ones = 0
        for num in data:
            if num == 1:
                num_ones += 1
                
        if num_ones == 1 or num_ones == 0:
            return 0
        
        for right in range(len(data)):
            if data[right] == 0:
                num_swaps += 1
            
            if right - left + 1 == num_ones:
                min_swaps = min(min_swaps, num_swaps)
                left += 1
                
                if left <= right and data[left - 1] == 0:
                    num_swaps -= 1  
            
        return min_swaps