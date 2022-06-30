# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) time complexity where n is the number of nodes
        # O(1) space complexity as no additional space is required
        
        curr_new_sum_node = None
        curr_sum = 0
        head = head.next
        curr_node = head
        while curr_node:
            if curr_node.val == 0:
                curr_new_sum_node.val = curr_sum
                curr_new_sum_node.next = curr_node.next
                curr_node = curr_new_sum_node.next
                curr_new_sum_node = None
                curr_sum = 0
            else:
                if not curr_new_sum_node:
                    curr_new_sum_node = curr_node
                curr_sum += curr_node.val
                curr_node = curr_node.next
        return head