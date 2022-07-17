# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(N) time complexity
# O(N) space complexity
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[0]
    
    def dfs(self, root: Optional[TreeNode]) -> Tuple[int, List[int]]:
        if not root.left and not root.right:
            return (1, [root.val])
        
        avg_left = avg_right = 0
        past_left_nodes = past_right_nodes = []
        
        if root.left:
            avg_left, past_left_nodes = self.dfs(root.left)
        if root.right:
            avg_right, past_right_nodes = self.dfs(root.right)
        
        left_len = len(past_left_nodes)
        right_len = len(past_right_nodes)
        n = left_len + right_len + 1
        
        n_nodes = past_left_nodes + past_right_nodes + [root.val]
        
        if sum(n_nodes) // n == root.val:
            return (avg_left + avg_right + 1, n_nodes)
        else:
            return (avg_left + avg_right, n_nodes)