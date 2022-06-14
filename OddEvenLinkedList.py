# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) time and O(1) space complexity
        node = 1
        prev_odd_node = curr_even_node = temp_node = None
        
        curr_node = head
        while curr_node:
            if node % 2 == 0:
                curr_even_node = curr_node
                curr_node = curr_node.next
            else:
                if not prev_odd_node: 
                    prev_odd_node = curr_node
                    curr_node = curr_node.next
                else:
                    temp_node = curr_node.next
                    curr_node.next = prev_odd_node.next
                    prev_odd_node.next = curr_node
                    curr_even_node.next = temp_node
                    prev_odd_node = prev_odd_node.next
                    curr_node = curr_even_node.next

                
            node += 1
            
        return head