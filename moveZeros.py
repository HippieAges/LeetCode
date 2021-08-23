class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx, counter = 0, 0
        for idx in range(n):
            if nums[idx] != 0:
                nums[idx], nums[counter] = nums[counter], nums[idx]
                counter += 1
            
        # while counter < n:
        #     if (val := nums[idx]) == 0:
        #         nums.append(nums.pop(idx)) # O(n) to remove and O(1) to append
        #     else:
        #         idx += 1
        #     counter += 1