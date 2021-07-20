class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = ""
        
        while columnNumber > 0:
            letter_val = columnNumber if columnNumber <= 26 else 26 if columnNumber % 26 == 0 else columnNumber % 26
            prev_total = 0 if columnNumber - letter_val == 0 else (columnNumber - letter_val) // 26
            letter = chr(ord('A') + letter_val - 1)
            letters = letter + letters
            columnNumber = prev_total
        

        return letters