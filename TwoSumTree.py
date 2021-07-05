class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        elements = set()
        
        def storeNodes(root: TreeNode, k: int, elements: set) -> bool:
            if root == None:
                return False
            second_elem = k - root.val
            if elements.__contains__(second_elem):
                return True
            else:
                elements |= {root.val}

            return (storeNodes(root.left, k, elements) or storeNodes(root.right, k, elements))
        
        return storeNodes(root, k, elements)