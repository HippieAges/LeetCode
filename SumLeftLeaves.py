# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def sumHelper(root: TreeNode, side: str) -> int:
            if root == None:
                return 0
            if root.left == None and root.right == None and side == "left":
                return root.val

            return sumHelper(root.left, "left") + sumHelper(root.right, "right")
        return sumHelper(root, "left")

s = Solution()
t9 = TreeNode(9)
t15 = TreeNode(15)
t7 = TreeNode(7)
t20 = TreeNode(20, left=t15, right=t7)
t3 = TreeNode(3, left=t9, right=t20)
print(s.sumOfLeftLeaves(t3))