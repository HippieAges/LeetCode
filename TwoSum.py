from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for index, element in enumerate(nums):
            value = target - element
            if (first_elem := hash_table.get(value, None)) != None: # Walrus operator only works in Python 3.8=
                return [first_elem, index] 
            hash_table[element] = index

c = Solution()
print(c.twoSum([2,7,11,15], 9))
print(c.twoSum([3,2,4], 6))
print(c.twoSum([3,3], 6))