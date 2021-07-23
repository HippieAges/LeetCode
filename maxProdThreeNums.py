class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # nums.sort(reverse=True)
        # two_num_product = nums[1] * nums[2] if nums[1] * nums[2] >= nums[-1] * nums[-2] or nums[0] < 0 else nums[-1] * nums[-2]
        # return nums[0] * two_num_product
        num1_min, num2_min = 1001, 1001
        num1_max, num2_max, num3_max = -1001, -1001, -1001
        
        for num in nums:
            
            if num < num1_min:
                num2_min = num1_min
                num1_min = num
            elif num < num2_min:
                num2_min = num
                
            if num > num1_max:
                num3_max = num2_max
                num2_max = num1_max
                num1_max = num
            elif num > num2_max:
                num3_max = num2_max
                num2_max = num
            elif num > num3_max:
                num3_max = num
            
        return max(num1_max * num1_min * num2_min, num1_max * num2_max * num3_max)