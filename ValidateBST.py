# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(Vh) time complexity where V is the vertices & h is the height of the tree
# O(h) space complexity
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)
    
    def dfs(self, root: Optional[TreeNode], nodes: List[Tuple[int, str]] = []) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return self._check_nodes(root, nodes)
        
        valid_left_bst = self.dfs(root.left, nodes + [(root.val, "left")])
        
        valid_right_bst = False
        if valid_left_bst and self._check_nodes(root, nodes):
            valid_right_bst = self.dfs(root.right, nodes + [(root.val, "right")])
        
        return valid_right_bst
        
    def _check_nodes(self, root: Optional[TreeNode], nodes: List[Tuple[int, str]]) -> bool:
            for node_val, direction in nodes:
                if direction == "left" and root.val >= node_val:
                    return False
                if direction == "right" and root.val <= node_val:
                    return False
            return True