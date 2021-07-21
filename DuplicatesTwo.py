from collections import OrderedDict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        occurrences = OrderedDict()
                
        for num in nums:
            occurrences[num] = occurrences.get(num, 0) + 1
            occurrences.move_to_end(num, last=False)
            if occurrences[num] == 2:
                return True
            if len(occurrences) == k + 1:
                occurrences.popitem()
        return False