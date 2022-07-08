class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # O(n * m) runtime complexity where n represents the # of digits in num1 & m represents the # of digits in num2
        # O(n + m) space complexity since strings are immutable in Python, so we need to store the reversed strings as well
        current_place = 0
        result = 0
        
        # reverse both strings
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        # now loop over both nums and perform the multiplication digit by digit
        for num1_idx, num1_digit in enumerate(num1):
            current_place = num1_idx
            for num2_digit in num2:
                result += int(num1_digit) * int(num2_digit) * (10 ** current_place)
                current_place += 1
                 
        return str(result)