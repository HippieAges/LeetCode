class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        nNode = head
        
        while nNode != None:
            count += 1
            nNode = nNode.next
        
        currentCount = count
        nNode = head
        
        while nNode != None:
            
            if currentCount - 1 == n:
                nNode.next = nNode.next.next
                break
            elif currentCount == n:
                head = head.next
                break
            
            currentCount -= 1
            nNode = nNode.next
        
        return head