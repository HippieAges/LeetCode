from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p_len = len(p)
        s_len = len(s)
        
        if p_len > s_len:
            return []
        
        # counts = Counter(s[:p_len])
        s_counts = Counter()
        p_counts = Counter(p)
        anagrams = []
        # r, l = p_len - 1, 0
        
        for i in range(s_len):
            s_counts[ s[i] ] += 1
            
            if i >= p_len:
                if s_counts[ s[i - p_len] ] == 1:
                    del s_counts[ s[i - p_len] ]
                else:
                    s_counts[ s[i - p_len] ] -= 1
        
            if s_counts == p_counts:
                anagrams.append( i - p_len + 1 )
        return anagrams
        
        # my solution from earlier -> slightly slower than above solution, but uses less memory
#         while r < s_len:
#             if counts == p_counts:
#                 anagrams.append(l)
#             if counts[ s[l] ] == 1:
#                 del counts[ s[l] ]
#             else:
#                 counts[ s[l] ] -= 1
            
#             l += 1
#             r += 1
            
#             if r < s_len:
#                 if not counts[ s[r] ]:
#                     counts[ s[r] ] = 1
#                 else:
#                     counts[ s[r] ] += 1
    
#         return anagrams