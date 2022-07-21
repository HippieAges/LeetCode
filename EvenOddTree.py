from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(V) time complexity
# O(V) space complexity
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        nodes = deque([(root, 0)])
        queue = deque([(root, 0)])
        prev_val = 0
        level_type = "odd"
        level = 0
        
        while nodes:
            top_node, _ = nodes.popleft()
            
            if top_node.left:
                nodes.append((top_node.left, level + 1))
                queue.append((top_node.left, level + 1))
            if top_node.right:
                nodes.append((top_node.right, level + 1))
                queue.append((top_node.right, level + 1))
            
            while queue and queue[0][1] == level:
                front, _ = queue.popleft()
                # print(front.val, level, prev_val, level_type)
                if prev_val:
                    if level_type == "even" and prev_val <= front.val:
                        return False
                    if level_type == "odd" and prev_val >= front.val:
                        return False
                if level_type == "even" and front.val % 2 != 0:
                    return False
                if level_type == "odd" and front.val % 2 == 0:
                    return False
                prev_val = front.val
            
            if nodes and level != nodes[0][1]:
                level += 1
                level_type = "even" if level_type == "odd" else "odd"
            prev_val = 0
            
        return True