# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) time and O(1) space complexity
        return self.swapPairsWithCount(1, head)
    
    def swapPairsWithCount(self, count: int, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        returned_node = self.swapPairsWithCount(count + 1, head.next)
        
        # if odd, then swap nodes
        if not ((count % 2) == 0):
            temp_node = returned_node.next
            returned_node.next = head
            head.next = temp_node
            return returned_node
        else: # otherwise just update the next reference to the newly swapped node
            head.next = returned_node
            return head
        