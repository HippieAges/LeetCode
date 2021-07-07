class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root == None:
            return 0
        
        left_node = self.rangeSumBST(root.left, low, high)
        right_node = self.rangeSumBST(root.right, low, high)
        
        if high >= root.val >= low:
            return root.val + left_node + right_node
        
        return left_node + right_node