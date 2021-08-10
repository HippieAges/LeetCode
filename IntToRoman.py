class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), 
                   ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), 
                   ("X", 10), ("IX", 9), ("V",5), ("IV", 4), ("I", 1)]
        roman_numerals = ""
        
        for roman, value in symbols:
            if value > num:
                continue
                
            count = num // value
            roman_numerals += roman*count
            num -= value*count
            
        return roman_numerals