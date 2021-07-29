class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        letter_combinations = []
        
        def backtrack(combination: List[str], index: int) -> None:
            if index == len(digits):
                letter_combinations.extend(combination.copy())
                return
            
            for letter in digits_to_letters[digits[index]]:
                if not combination:
                    combination.append(letter)
                else:
                    combination[0] += letter
                index += 1
                backtrack(combination, index)
                index -= 1
                combination[0] = combination[0][:index]
                
        backtrack([], 0)
        return letter_combinations