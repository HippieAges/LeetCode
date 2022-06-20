# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) time and O(1) space complexity
        
        
        # count number of nodes to get n
        curr_node = head
        n = 0 
        while curr_node:
            n += 1
            curr_node = curr_node.next
        
        mid_node = n // 2 # implicitly floor of n / 2
        
        prev_node = None
        curr_node = head
        curr_node_idx = 0
        
        if curr_node_idx == mid_node:
            return None
        
        while curr_node:
            prev_node = curr_node
            curr_node = curr_node.next
            curr_node_idx += 1
            
            if curr_node_idx == mid_node:
                prev_node.next = curr_node.next
                curr_node.next = None
                break
        return head