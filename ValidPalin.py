class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reversedStr, modifiedStr = "", "" # for second solution
        index = 0
        reversedIndex = len(s) - 1
        
        
        while index < reversedIndex:
            if not s[index].isalnum():
                index += 1
                continue
            if not s[reversedIndex].isalnum():
                reversedIndex -= 1
                continue
            
            if s[index].lower() != s[reversedIndex].lower():
                return False
            
            index += 1
            reversedIndex -= 1
        
        return True

        # second solution:
        # for character in s:
        #     if character.isalnum():
        #         modifiedStr += character.lower()
    
        # for character in modifiedStr[::-1]:
        #     reversedStr += character
                    
        # return reversedStr == modifiedStr