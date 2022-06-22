# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) time and O(1) space complexity
        
        # get the midpt
        n = 0
        curr_node = head
        while curr_node:
            n += 1
            curr_node = curr_node.next
        
        midpt = n // 2
        
        # now retrieve the head
        curr_node = head
        node_idx = 0
        while curr_node:
            if node_idx == midpt:
                return curr_node
            node_idx += 1
            curr_node = curr_node.next
        
        return curr_node