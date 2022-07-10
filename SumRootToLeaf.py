# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # O(V + E) time complexity since we run DFS and cover each vertex and edge exactly once
        # O(P) space complexity where P is the # of paths that exist from root to leaf node
        
        return sum(map(lambda path: int(path), self.dfs(root, paths = [])))
        
    def dfs(self, root: Optional[TreeNode], current_path = "", paths = []) -> List[int]:
        if not root.left and not root.right:
            paths.append(current_path + f"{root.val}")
            return paths
        
        current_path += f"{root.val}"
        
        if root.left:
            self.dfs(root.left, current_path, paths)
        if root.right:
            self.dfs(root.right, current_path, paths)
        
        return paths