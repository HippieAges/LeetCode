# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # O(n) time and O(n) space complexity 
        critical_pts = []
        curr_node = head
        prev_node = None
        next_node = curr_node.next
        node = 1
        while next_node:
            prev_node = curr_node
            curr_node = curr_node.next
            next_node = curr_node.next
            
            if prev_node and next_node:
                if (prev_node.val > curr_node.val and next_node.val > curr_node.val) or \
                   (curr_node.val > prev_node.val and curr_node.val > next_node.val):
                    critical_pts.append(node)
            node += 1
        
        # if fewer than 2 critical pts, return [-1, -1]
        if len(critical_pts) < 2:
            return [-1, -1]
        
        max_dist = critical_pts[-1] - critical_pts[0]
        min_dist = float("inf")
        sub_op = 0
        
        for idx in range(len(critical_pts) - 1):
            sub_op = critical_pts[idx + 1] - critical_pts[idx]
            if min_dist > sub_op:
                min_dist = sub_op
        return [min_dist, max_dist]