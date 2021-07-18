class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return False
        if head.next == None:
            return True
        
        def iterateBoth(head: ListNode, tail: ListNode) -> Union[None, ListNode]:
            if tail.next == None:
                return head.next if head.val == tail.val else None
            
            headNode = iterateBoth(head, tail.next)
            if not headNode or headNode.val != tail.val:
                return None
            return ListNode() if headNode.next == None else headNode.next 
        
        return iterateBoth(head, head) != None