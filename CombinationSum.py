from collections import Counter
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combinations = []
        all_unique_combs = []
        
        def backtrack(remaining : int, combination : List[int], all_unique_combs : List[Counter]) -> None:
            if remaining == 0: # if we have reached n == 0, then we have found a possible unique combination
                
                unique_comb = True
                comb_copy = combination.copy()
                possible_unique_comb = Counter(combination)
                
                for unique_comb in all_unique_combs:
                    if unique_comb == possible_unique_comb:
                        unique_comb = False
                        break
                
                if unique_comb:
                    all_unique_combs.append(possible_unique_comb)
                    combinations.append(comb_copy)
                return
            elif remaining < 0: # if we're less than 0, then we just return since we can't add to the list
                return
            
            for candidate in candidates:
                combination.append(candidate)
                backtrack(remaining - candidate, combination, all_unique_combs)
                combination.pop()
                
        backtrack(target, [], all_unique_combs)
        
        return combinations