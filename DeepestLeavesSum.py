# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_depth = self._getDepth(root, 0)
        
        # O(V) time complexity to visit each node once
        # O(1) space complexity as we don't allocate space for a ds 
        def sumLeaves(root: Optional[TreeNode], curr_depth: int) -> int:
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val if curr_depth >= max_depth else 0
            
            return sumLeaves(root.left, curr_depth + 1) + sumLeaves(root.right, curr_depth + 1)
        return sumLeaves(root, 0)
    
    # O(V) time complexity to visit each node once
    # O(1) space complexity as we don't allocate space for a ds
    def _getDepth(self, root: Optional[TreeNode], curr_depth: int) -> int:
        if not root:
            return curr_depth - 1
        if not root.left and not root.right:
            return curr_depth
        
        left_depth = self._getDepth(root.left, curr_depth + 1)
        right_depth = self._getDepth(root.right, curr_depth + 1)
        
        return left_depth if left_depth > curr_depth and left_depth > right_depth else right_depth