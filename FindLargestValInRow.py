from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        return self.dfs(root, 0, [])
          # O(V + E) time complexity
          # O(V) space complexity
#         if not root:
#             return []
        
#         queue = deque([(root, 1)])
#         nodes = deque([(root, 1)])
#         level = 1
#         largest_num_in_row = float("-inf")
#         result = []
        
#         while nodes:
            
#             node, _ = nodes.popleft()
            
#             if node.left:
#                 queue.extend([(node.left, level + 1)])
#                 nodes.extend([(node.left, level + 1)])
#             if node.right:
#                 queue.extend([(node.right, level + 1)])
#                 nodes.extend([(node.right, level + 1)])
            
#             while len(queue) > 0 and level == queue[0][1]:
#                 curr_node, _ = queue.popleft()    
#                 if curr_node.val > largest_num_in_row:
#                     largest_num_in_row = curr_node.val
            
#             if largest_num_in_row != float("-inf"):
#                 result.append(largest_num_in_row)
#             largest_num_in_row = float("-inf")
#             # print(result)
#             if nodes:
#                 level = nodes[0][1] 
            
#         return result
    
    # O(V + E) time complexity
    # O(1) space complexity
    def dfs(self, root: Optional[TreeNode], level, result = []) -> List[int]:
        if not root:
            return []
        
        if level > len(result) - 1:
            result.append(root.val)
        elif root.val > result[level]:
            result[level] = root.val
        # print(result)
        if not root.left and not root.right:
            return result
        
        if root.left:
            result = self.dfs(root.left, level + 1, result)
        if root.right:
            result = self.dfs(root.right, level + 1, result)
        
        return result
            