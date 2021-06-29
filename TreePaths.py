# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return []
        
        paths = []
        
        def addingToPath(root: TreeNode, path: str) -> None:
            if root.left == None and root.right == None:
                paths.append(f"{path}{root.val}")
                return
            elif root.right == None and root.left != None:
                addingToPath(root.left, f"{path}{root.val}->")
                return
            elif root.right != None and root.left == None:
                addingToPath(root.right, f"{path}{root.val}->")
                return
            else:
                addingToPath(root.left, f"{path}{root.val}->")
                addingToPath(root.right, f"{path}{root.val}->")
                return
        
        addingToPath(root, "")
        return paths