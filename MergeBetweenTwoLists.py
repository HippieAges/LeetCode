# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # O(n) time and O(1) space complexity
        
        before_ath_node = after_bth_node = None
        curr_node_list1 = list1
        node_idx = 0
        while curr_node_list1:
            if node_idx == a - 1:
                before_ath_node = curr_node_list1
            if node_idx == b + 1:
                after_bth_node = curr_node_list1
                break
            curr_node_list1 = curr_node_list1.next
            node_idx += 1
            
        prev_node = None
        curr_node_list2 = before_ath_node.next = list2 # the a - 1 node.next -> list2.head
        
        while curr_node_list2:
            prev_node = curr_node_list2
            curr_node_list2 = curr_node_list2.next
        
        if prev_node: # if there is a prev_node then the prev_node.next -> b + 1 node
            prev_node.next = after_bth_node
        
        return list1