from math import ceil

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # O(n) time and O(1) space complexity 
        
        # get the midpt in the list
        curr_node = head
        n = 1
        while curr_node:
            curr_node = curr_node.next
            n += 1
        
        mid_pt = ceil(n // 2)
        
        def helper(head: Optional[ListNode], tail: Optional[ListNode]) -> Tuple[Optional[ListNode], int]:
            if not tail.next:
                return (head, tail, 1)

            curr_head, curr_tail, idx = helper(head, tail.next)

            if idx == mid_pt:
                return (head, head, idx)

            temp_node = curr_head.next
            curr_head.next = curr_tail
            curr_tail.next = temp_node
            tail.next = None

            return (temp_node, tail, idx + 1)
        
        # iterate from front to back while going back to front also
        return helper(head, head)[0]