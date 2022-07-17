# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(h) time complexity where h is the height of the tree
# O(1) space complexity
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def helper(root: Optional[TreeNode], parent: Optional[TreeNode], side: str, key: int) -> Optional[TreeNode]:
            if not root:
                return None

            if key == root.val:
                if root.right and root.left:
                    if side == "left":
                        parent.left = root.right
                        self.get_left_tree_node(root.right).left = root.left
                        return parent.left
                    elif side == "right":
                        parent.right = root.right
                        self.get_left_tree_node(root.right).left = root.left
                        return parent.right
                    else:
                        prior_left_node = root.left
                        root = root.right
                        self.get_left_tree_node(root).left = prior_left_node
                        return root
                elif root.left:
                    return root.left
                elif root.right:
                    return root.right
                else: # not root.left and not root.right
                    return None
            elif key < root.val:
                root.left = helper(root.left, root, "left", key)
            else: # key > root.val
                root.right = helper(root.right, root, "right", key)
            return root
            
        return helper(root, root, None, key)
    
    def get_left_tree_node(self, root: Optional[TreeNode]) -> TreeNode:
        if not root.left:
            return root
        
        return self.get_left_tree_node(root.left)