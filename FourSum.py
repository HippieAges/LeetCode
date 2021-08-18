class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        quadruplets = set()
        
        for a in range(n):
            for b in range(a + 1, n):
                self.twoSum(nums, res, (a, b, target), quadruplets)
        return res
                
    def twoSum(self, nums: List[int], res: List[List[int]], targets: Tuple[int], quadruplets: set) -> None: 
        a, b, target = targets
        low, high = b + 1, len(nums) - 1
        quadruplet = ()
        
        while low < high:
            sum_ = nums[a] + nums[b] + nums[low] + nums[high]
            quadruplet = (nums[a], nums[b], nums[low], nums[high])
            
            if sum_ == target and quadruplet not in quadruplets:
                res.append([nums[a], nums[b], nums[low], nums[high]])
                quadruplets.add(quadruplet)
                low += 1
                high -= 1
                
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
            elif quadruplet in quadruplets:
                low += 1
                high -= 1
            elif sum_ < target:
                low += 1
            elif sum_ > target:
                high -= 1  