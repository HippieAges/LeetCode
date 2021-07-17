class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # recursive solution
        if head == None or head.next == None:
            return head
        
        nextNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return nextNode
        # iterative solution
#         tempHead = newHead = ListNode(head.val)
        
#         while head.next != None:
#             head = head.next
#             tempHead = newHead
#             newHead = ListNode(head.val)
#             newHead.next = tempHead
            
#         return newHead