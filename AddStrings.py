class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # O(n) runtime complexity where n is the longer num with most characters
        # O(n + m) space complexity since we're creating new strings storing num1 & num2 reversed
        
        # reverse the two strings
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        result = 0
        other_digit_idx = 0
        num1_is_longer = True
        longer_num = num1
        
        if len(num1) < len(num2):
            longer_num = num2
            num1_is_longer = False        
        
        for idx, digit in enumerate(longer_num):
            if num1_is_longer and other_digit_idx < len(num2):
                result += (int(digit) * (10 ** idx)) + (int(num2[other_digit_idx]) * (10 ** idx))
            elif not num1_is_longer and other_digit_idx < len(num1):
                result += (int(digit) * (10 ** idx)) + (int(num1[other_digit_idx]) * (10 ** idx))
            else:
                result += int(digit) * (10 ** idx)
            other_digit_idx += 1
                
        return str(result)