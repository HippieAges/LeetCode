from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        num_table = Counter(nums)
        num_len = len(nums)
        
        def backtrack(permutation: List[int], counter: List[Tuple[int, int]]) -> None:
            if len(permutation) == num_len:
                # print("check permutations:", permutations)
                permutations.append(permutation.copy())
                return
            
            for i in range(0, len(counter)):
                num, freq = counter[i]
                # print(num, freq)
                if freq <= 0:
                    continue
                    
                permutation.append(num)
                counter[i] = (num, freq - 1)
                # print("check counter[i] before:", counter[i])
                # print("check num & freq before:", num, freq)
                backtrack(permutation, counter)
                # print("Check num & freq after:", num, freq)
                counter[i] = (num, freq)
                permutation.pop()
                # print("check counter[i] after:", counter[i])
                
        counter = [(c, num_table[c]) for c in num_table]
        # print(counter)
        backtrack([], counter)
        return permutations