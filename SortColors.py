class Solution:
    from collections import Counter
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute-force solution: bubble sort - O(n^2) time and O(1) space
        # for i in range(len(nums)):
        #     swapped = False
        #     for j in range(0, len(nums) - 1 - i):
        #         if nums[j] > nums[j + 1]:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        #             swapped = True
        #     if not swapped:
        #         break
                
        # better solution: counting sort using the Counter object - O(n) time and O(n) space
        occurrences = Counter(nums)
        colors = [2,1,0]
        index = 0
        while len(occurrences) > 0:
            last_color = colors[-1]
            if occurrences[last_color] > 0:
                nums[index] = last_color
                occurrences[last_color] -= 1
                index += 1
            if occurrences[last_color] == 0:
                colors.pop()
            if occurrences[last_color] == 0:
                del occurrences[last_color]