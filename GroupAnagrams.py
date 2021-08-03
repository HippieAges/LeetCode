from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through the list and sort each string 
        # and store the sorted string as a key and the index
        # + unsorted string as a tuple pair
        # runtime is O(n^2log(n) + n^2)
        # space complexity is O(n + n)
        
        if len(strs) == 1:
            return [[strs[0]]]
        
        sorted_strs = defaultdict(list)
        anagrams = []
        
        for idx, curr_str in enumerate(strs):
            sorted_str = reduce(lambda x, y: x + y, sorted(curr_str)) if curr_str else ""
            sorted_strs[sorted_str].append( (curr_str, idx) )
            
        for key in sorted_strs:
            anagrams.append([curr_str for curr_str, _ in sorted_strs[key] ])
        
        return anagrams