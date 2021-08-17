class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        curr_nums = {}
        
        for idx, num in enumerate(numbers):
            if (first_elem := target - num) in curr_nums:
                return [curr_nums[first_elem] + 1, idx + 1]
            curr_nums[num] = idx