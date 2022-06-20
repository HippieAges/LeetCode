# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # O(n) time and O(1) space complexity
        
        # get the midpt
        curr_node = head
        n = 0
        while curr_node:
            n += 1
            curr_node = curr_node.next
        
        mid_pt = n // 2
        
        def helper(head: Optional[ListNode], tail: Optional[ListNode]) -> Tuple[Optional[ListNode], int, int]:
            if not tail:
                return (head, 0, 0)
            
            curr_node, curr_sum, node_idx = helper(head, tail.next)
            
            if node_idx == mid_pt:
                return (head, curr_sum, node_idx)
            
            if (greater_sum := curr_node.val + tail.val) > curr_sum:
                return (curr_node.next, greater_sum, node_idx + 1)
            else:
                return (curr_node.next, curr_sum, node_idx + 1)
            
        return helper(head, head)[1]
            