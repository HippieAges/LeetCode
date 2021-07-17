class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = dict()
        
        for num in nums:
            elements[num] = elements.get(num, 0) + 1
            
        return max(elements.items(), key=lambda element: element[1])[0]