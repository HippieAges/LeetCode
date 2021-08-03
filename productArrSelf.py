class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute-force solution
#         products = []
        
#         for i in range(len(nums)):
#             product = 1
#             for j in range(len(nums)):
#                 if i == j:
#                     continue
#                 product *= nums[j]
#             products.append(product)
        
#         return products

        running_product = 1
        ans = []
        
        # go forward
        for idx in range(len(nums)):
            self_product = running_product
            ans.append(self_product)
            running_product *= nums[idx]
        
        running_product = 1
        
        # go backwards
        for idx in range(len(nums) - 1, -1, -1):
            self_product = running_product
            ans[idx] *= self_product
            running_product *= nums[idx]
        
        # print(ans)
        return ans