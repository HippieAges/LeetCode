# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def countGoodNodes(root: TreeNode, maxNode: int) -> int:
            if not root:
                return 0
            if not root.left and not root.right:
                return 1 if root.val >= maxNode else 0
            
            if root.val > maxNode:
                maxNode = root.val
                
            left = countGoodNodes(root.left, maxNode)
            right = countGoodNodes(root.right, maxNode)
            
            if root.val < maxNode:
                return left + right
            else:
                return left + right + 1
            
        return countGoodNodes(root, root.val)