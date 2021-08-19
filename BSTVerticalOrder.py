# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        correct_order = defaultdict(list)
        order = self.traversal(root, 0)
        order.sort(key=lambda x: x[1])
        for elem, index in order:
            correct_order[index].append(elem)
        
        return correct_order.values()
        
    def traversal(self, root: Optional[TreeNode], orderValue: int) -> List[Tuple[int]]:
        queue = deque([(root, 0)])
        order = []
        
        while queue:
            node, order_val = queue.popleft()
            order.append((node.val, order_val))
        
            if node.left or node.right:
                if node.left:
                    queue.append((node.left, order_val - 1))
                if node.right:
                    queue.append((node.right, order_val + 1))
        
        return order