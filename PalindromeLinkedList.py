class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return False
        
        def iterateBoth(head: ListNode, tail: ListNode) -> Union[bool, ListNode, ListNode]:
            if tail.next == None:
                if head.val == tail.val:
                    return head.next
                else:
                    return False
            
            headNode = iterateBoth(head, tail.next)
            if headNode == False or headNode.val != tail.val:
                return False
            return headNode.next
            
        return True if iterateBoth(head, head) != False else False