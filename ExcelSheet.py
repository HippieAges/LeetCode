class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        prev_total = 0
        for letter in columnTitle:
            letter_val = ord(letter) - ord('A') + 1
            total = letter_val + 26 * prev_total
            prev_total = total
        return total