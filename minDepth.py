# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        left_node_val = self.minDepth(root.left)
        right_node_val = self.minDepth(root.right)
        
        if left_node_val != 0 and right_node_val != 0: 
            return 1 + min(left_node_val, right_node_val)
        elif left_node_val != 0:
            return 1 + left_node_val
        return 1 + right_node_val