class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
        unique_nums = set()
        num_len = len(nums)
        
        def backtrack(permutation: List[int], unique_nums: set) -> None:
            if len(permutation) == num_len:
                permutations.append(permutation.copy())
                return
            
            for i in range(0, num_len):
                
                if nums[i] in unique_nums:
                    continue
            
                unique_nums |= {nums[i]}
                permutation.append(nums[i])
                backtrack(permutation, unique_nums)
                permutation.pop()
                unique_nums.remove(nums[i])
                
            
        backtrack([], unique_nums)
        return permutations