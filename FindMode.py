# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        nodes = {}
        
        def traverseTree(root: TreeNode) -> None:
            if root == None:
                return
            
            traverseTree(root.left)
            traverseTree(root.right)
            
            
            nodes[root.val] = nodes.get(root.val, 0) + 1
            return
        
        traverseTree(root)
        sorted_nodes = sorted(nodes.items(), key=lambda item: item[1], reverse=True)
        return [node for node, mode in sorted_nodes if mode == sorted_nodes[0][1]]
        # return [max(nodes, key=lambda key: nodes[key])]