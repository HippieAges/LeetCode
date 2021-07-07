class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
          # solution using BFS  
#         queue = [root]
        
#         while len(queue) > 0:
#             current_node = queue.pop(0)
#             if current_node != None:
#                 if current_node.val == val:
#                     return current_node
#                 queue.append(current_node.left)
#                 queue.append(current_node.right)
#         return None
    
        if root == None:
            return None
        
        if root.val == val:
            return root
        
        return (self.searchBST(root.left, val) or self.searchBST(root.right, val))