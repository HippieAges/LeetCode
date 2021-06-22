# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # gets the height of both trees: not used here
    def getHeight(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        return max(left_height, right_height) + 1

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root == None:
            return False
        elif self.inBothTrees(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def inBothTrees(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root == None and subRoot == None:
            return True
        elif root == None or subRoot == None:
            return False
        else:
            return root.val == subRoot.val and self.inBothTrees(root.left, subRoot.left) and self.inBothTrees(root.right, subRoot.right)