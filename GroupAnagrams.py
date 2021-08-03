from collections import defaultdict
from itertools import reduce
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through the list and sort each string 
        # and store the sorted string as a key and the index
        # + unsorted string as a tuple pair
        # runtime is O(nklog(k))
        # space complexity is O(nk)
        
        if len(strs) == 1:
            return [[strs[0]]]
        
        sorted_strs = defaultdict(list)
        
        for curr_str in strs:
            sorted_str = reduce(lambda x, y: x + y, sorted(curr_str)) if curr_str else ""
            sorted_strs[sorted_str].append(curr_str)
        
        return sorted_strs.values()