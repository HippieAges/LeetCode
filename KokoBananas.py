from __future__ import annotations
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute-force solution
        # O(n*m) time where n = piles of bananas & m = max(piles[0] ... piles[len(piles) - 1]) 
        # O(m) space complexity
        # exceeds time limit
        
#         possible_ks = (elem for elem in range(1, max(piles) + 1))
#         k = 0
#         temp_h = h
        
#         for possible_k in possible_ks:
#             for idx, bananas in enumerate(piles):
#                 temp_h -= ceil(bananas / possible_k)
#                 if temp_h < 0 or (temp_h == 0 and idx != len(piles) - 1):
#                     temp_h = h
#                     break
#                 elif temp_h >= 0 and bananas == piles[-1]:
#                     return possible_k
        
#         return k
        # optimized solution (not the best)
        # O(mlogn) time & O(1) space complexity
        def binary_search(low_k: int, high_k: int) -> int:
            temp_h, mid_k = 0, 1
            smallest_pos_temp_h, temp_mid_k = high_k, 1
            while low_k <= high_k:
                mid_k = (low_k + high_k) // 2
                temp_h = h
                for bananas in piles:
                    temp_h -= ceil(bananas / mid_k)
                if temp_h < 0:
                    low_k = mid_k + 1
                elif temp_h > 0:
                    high_k = mid_k - 1
                else:
                    high_k = mid_k - 1
                    temp_mid_k = mid_k # needed since when tem_h = 0, we didn't necessarily find the smallest k value
                if temp_h > 0 and temp_h < smallest_pos_temp_h:
                    smallest_pos_temp_h = temp_h
                    temp_mid_k = mid_k
            return temp_mid_k
        
        return binary_search(1, max(piles))