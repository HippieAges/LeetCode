# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # applies only to preorder traversal
    def traversal(self, preOrder: list[int], root: TreeNode) -> list[int]:
        rightElements = []

        while True:
            if root != None:
                if root.right != None:
                    rightElements.append(root.right)
                root = root.left
            if len(rightElements) > 0 and root == None:
                root = rightElements.pop()

            if root == None:
                break
            preOrder.append(root.val)
        return preOrder

    # iterative & recursive solution provided
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if root == None:
            return []

        preOrder = [root.val]
        return self.traversal(preOrder, root)
        
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) # recursive solution

    # 
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if root == None:
            return []
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] # recursive solution

s = Solution()
# t1 = TreeNode(3)
# t2 = TreeNode(2, left=t1)
# t3 = TreeNode(1, right=t2)
# print(s.postorderTraversal(t3))

# t2 = TreeNode(2)
# t3 = TreeNode(1, left=t2)
# print(s.postorderTraversal(t3))

# t3 = TreeNode(1, right=t2)
# print(s.postorderTraversal(t3))

# t4 = TreeNode(4)
# t5 = TreeNode(5)
# t3 = TreeNode(3)
# t2 = TreeNode(2, left=t4, right=t5)
# t1 = TreeNode(1, left=t2, right=t3)
# print(s.postorderTraversal(t1))

# t1 = TreeNode(1)
# print(s.postorderTraversal(t1))

t8 = TreeNode(8)
t6 = TreeNode(6)
t7 = TreeNode(7, left=t8)
t5 = TreeNode(5, right=t6)
t4 = TreeNode(4, left=t5)
t2 = TreeNode(2, left=t4)
t3 = TreeNode(3, right=t7)
t1 = TreeNode(1, left=t2, right=t3)

print(s.postorderTraversal(t1))