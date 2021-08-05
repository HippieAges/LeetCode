class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sums = {0 : 1}
        ans = 0
        curr = 0
        for num in nums:
            curr += num
            if (val := sums.get(curr % k, 0)):
                ans += val
            sums[curr % k] = val + 1
        return ans