# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        deleted_node_val = float("-inf")
        prev_node = None
        curr_head = head
        while curr_head != None:
            if curr_head.next != None and curr_head.next.val == curr_head.val:
                deleted_node_val = curr_head.val
                if prev_node:
                    prev_node.next = curr_head.next
                    curr_head = prev_node
                else:
                    head = head.next
                    curr_head = head
            elif deleted_node_val == curr_head.val:
                if not prev_node:
                    head = head.next
                    curr_head = head
                else:
                    if not curr_head.next:
                        prev_node.next = None
                        curr_head = prev_node
                    else:
                        prev_node.next = curr_head.next
                        curr_head = prev_node
                deleted_node_val = float("-inf")  
            else:
                prev_node = curr_head
                curr_head = curr_head.next
            
        return head