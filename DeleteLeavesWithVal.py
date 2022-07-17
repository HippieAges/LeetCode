# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(N) time complexity
# O(1) space complexity
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        if not root.left and not root.right:
            return None if root.val == target else root
        
        root.left = self.removeLeafNodes(root.left, target)
        
        if not root.left and not root.right and root.val == target:
            return None
        
        root.right = self.removeLeafNodes(root.right, target)
        
        if not root.left and not root.right and root.val == target:
            return None
        
        return root