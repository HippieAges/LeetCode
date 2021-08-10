from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        basket1, basket2 = -1, -1
        max_len = 0
        fruits_len = len(fruits)
        
        hash_map = defaultdict(int)
        
        for right in range(fruits_len):
            hash_map[fruits[right]] += 1
            
            while left < fruits_len and len(hash_map) > 2:
                hash_map[fruits[left]] -= 1
                if hash_map[fruits[left]] == 0:
                    del hash_map[fruits[left]]
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len