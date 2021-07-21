class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring, l, r = 0, 0, 0
        count = [-1] * 256
        
        while r < len(s):
            character = ord(s[r])
            l = max(l, count[character] + 1)
            count[character] = r
            r += 1
            max_substring = max(max_substring, r - l)
        return max_substring