class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # iterate over all characters in s - 2 (as we don't want the last two values)
        # then if the current three characters aren't equal, add them to a list
        # finally, return the list length since it has non-repeating characters only
        
        if len(s) < 3:
            return 0
        
        all_substrings = []
        
        for index, character in enumerate(s[:len(s) - 2]):
            if character != s[index + 1] and character != s[index + 2] and s[index + 1] != s[index + 2]: 
                all_substrings.append((character, s[index + 1], s[index + 2]))
            
        return len(all_substrings)  