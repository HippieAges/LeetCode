# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # O(n) time and O(1) space complexity
        if not head:
            return None
        
        # get the length of the linked list
        num_nodes = 0
        curr_head = head
        while curr_head:
            num_nodes += 1
            curr_head = curr_head.next
        
        return self.helper(head, head, k % num_nodes)[0]
    
    def helper(self, head: Optional[ListNode], curr_node: Optional[ListNode], k: int) -> Tuple[ListNode, ListNode, int]:
        if not curr_node.next:
            return (head, curr_node, k)
        
        old_head, tail, updated_k = self.helper(head, curr_node.next, k)
        if updated_k == 0:
            return (old_head, tail, 0)
        
        prior_head = old_head
        old_head = tail
        curr_node.next = tail.next
        old_head.next = prior_head

        return (old_head, curr_node, updated_k - 1)
        