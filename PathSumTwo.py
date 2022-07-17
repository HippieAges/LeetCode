# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # O(V + E) runtime complexity
        #O(Vd) where V is the vertices and d is depth of the tree for space complexity - if the return list is considered part of the runtime
        # otherwise, O(d) space complexity
        paths = []
        
        def helper(root: Optional[TreeNode], targetSum: int, path: List[int] = []) -> List[List[int]]:
            if not root:
                return []
            
            if not root.left and not root.right:
                targetSum -= root.val
                if targetSum == 0:
                    path.append(root.val)
                    paths.append(path)   
                return paths
            
            # path.append(root.val)
            current_paths = []
            
            if root.left:
                current_paths = helper(root.left, targetSum - root.val, path + [root.val])
            if root.right:
                current_paths = helper(root.right, targetSum - root.val, path + [root.val])
            return current_paths
        
        return helper(root, targetSum)