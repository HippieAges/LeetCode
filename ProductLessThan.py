class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # keep a left and right index, increment the right index and increment the left
        # index when the previous product * current element >= k
        # keep track of the running product and if we need to adjust the left index, then
        # divide by the element at that index and continue until we're at a product < k
        if k <= 1:
            return 0
        
        l, r = 0, 0
        product = 1
        solution = 0
        while r < len(nums):
            product *= nums[r]
            while product >= k:
                product /= nums[l]
                l += 1
            solution += r - l + 1 # this one line was from the LeetCode solutions, I was so close to the solution :(
            r += 1
        return solution