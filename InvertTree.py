# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        if root.left == None and root.right == None:
            return root
        
        left_side = self.invertTree(root.left)
        right_side = self.invertTree(root.right)

        root.left, root.right = right_side, left_side
        return root