from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hash_map = defaultdict(int)
        left = 0
        ans = 0
        result = 0
        s_len = len(s)
        
        for right in range(s_len):
            hash_map[s[right]] += 1
            
            while left < s_len and 'a' in hash_map and 'b' in hash_map and 'c' in hash_map:
                ans += 1
                hash_map[s[left]] -= 1
                if hash_map[s[left]] == 0:
                    del hash_map[s[left]]
                left += 1
            result += ans
            
            
        return result