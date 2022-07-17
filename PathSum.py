# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # O(V + E) time complexity
        # O(1) space complexity
        
        if not root:
            return False
        
        if not root.left and not root.right:
            targetSum -= root.val
            return True if targetSum == 0 else False
        
        has_path = False
        if root.left:
            has_path = self.hasPathSum(root.left, targetSum - root.val)
        if root.right and not has_path:
            has_path = self.hasPathSum(root.right, targetSum - root.val)
        
        return has_path