# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # return self.dfs(root)[k - 1]
        
        return self.dfs(root, k)[0]
    # O(h + k) time complexity where h is the height of the binary tree
    # O(1) space complexity
    def dfs(self, root: Optional[TreeNode], k: int) -> Tuple[int, bool]:
        if not root:
            return (k, False)
        if not root.left and not root.right:
            k -= 1
            return (root.val, True) if k == 0 else (k, False)
        
        left_k_result, found_smallest_k = self.dfs(root.left, k)
        if found_smallest_k:
            return (left_k_result, True)
        curr_k_result = left_k_result - 1  
        if curr_k_result == 0:
            return (root.val, True)
        
        right_k_result, found_smallest_k = self.dfs(root.right, curr_k_result)
        if found_smallest_k:
            return (right_k_result, True)
        return (right_k_result, False)
    
    # O(N) time complexity
    # O(N) space complexity
#     def dfs(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         if not root.left and not root.right:
#             return [root.val]
        
#         return self.dfs(root.left) + [root.val] + self.dfs(root.right)