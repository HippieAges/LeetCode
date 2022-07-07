from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # O(V + E) time & O(V) space complexity
        # V represents the # of vertices in the binary tree
        # E represents the # of edges in the binary tree
        # since we visit each vertex and each edge only once, we get O(V + E)
        # O(V) for space complexity since we store each vertex eventually
        
        queue = deque()
        nodes = deque()
        
        if not root:
            return None
        
        queue.append((root, 1))
        nodes.append((root, 1))
        
        left = right = None
        level = queue[0][1]

        while nodes:
            left = right = None
            
            if nodes[0][0].left:
                queue.append((nodes[0][0].left, level + 1))
                nodes.append((nodes[0][0].left, level + 1))
            if nodes[0][0].right:
                queue.append((nodes[0][0].right, level + 1))
                nodes.append((nodes[0][0].right, level + 1))
                        
            while len(queue) > 0 and queue[0][1] == level:
                if left and not right:
                    right, _ = queue.popleft()
                elif not left:
                    left, _ = queue.popleft()    
                
                if left and right:
                    left.next = right
                    left = left.next
                    right = None
            
            nodes.popleft()
            if nodes:
                level = nodes[0][1]
        
        return root