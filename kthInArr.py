import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute-force solution
        # sort nums in descending order, then iterate over
        # nums and stop at the k + 1 element (since we index beginning at 0)
        # time is O(nlogn) and space is O(1)
        
        # nums.sort(reverse=True)
        # kth_elem = 0
        # for idx in range(len(nums)):
        #     k -= 1
        #     if k == 0:
        #         kth_elem = nums[idx]
        #         break
                
        # heap implementation
        # time is O(nlogk) and space is O(k) 
#         orig_nums = nums.copy()
#         heapq.heapify(nums)
#         kth_idx = len(nums) - k
#         # print(nums)
#         for idx in range(len(orig_nums)):
#             # print(nums[idx])
#             elem = heapq.heappop(nums)
#             if idx == kth_idx:
#                 kth_elem = elem
#                 break
        
#         return kth_elem
        # one-liner in Python
        return heapq.nlargest(k, nums)[-1]