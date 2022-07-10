# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # O(n) time complexity
        # O(1) space complexity
        
        # count # of nodes
        num_nodes = 0
        temp_node = head
        while temp_node:
            num_nodes += 1
            temp_node = temp_node.next   
            
        k_node_from_beginning = None
        k_node_from_end = None
        
        curr_node = head
        node_idx = 1
          
        while curr_node:
            if node_idx == k:
                k_node_from_beginning = curr_node
            if node_idx == num_nodes - k + 1:
                k_node_from_end = curr_node
            curr_node = curr_node.next
            node_idx += 1
        
        temp_node_val = k_node_from_beginning.val
        k_node_from_beginning.val = k_node_from_end.val
        k_node_from_end.val = temp_node_val
        
        return head