class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combinations = []
        
        def backtrack(remaining : int, combination : List[int], index : int):
            if remaining == 0: # if we have reached n == 0, then we have found a unique combination
                combinations.append(combination.copy())
                return
            elif remaining < 0: # if we're less than 0, then we just return since we have exceeded the target
                return 
            
            for i in range(index, len(candidates)):
                combination.append(candidates[i])
                index = backtrack(remaining - candidates[i], combination, i)
                combination.pop()
                
        backtrack(target, [], 0)
        
        return combinations