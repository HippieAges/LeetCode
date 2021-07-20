# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # have two pointers, one moves twice as fast as the previous one
        # if not fast.next and not fast then we don't have a cycle
        # this utilizes Floyd's Cycle Detection algorithm

        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
            
        return False