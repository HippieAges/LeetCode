class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        two_num_product = nums[1] * nums[2] if nums[1] * nums[2] >= nums[-1] * nums[-2] or nums[0] < 0 else nums[-1] * nums[-2]
        return nums[0] * two_num_product