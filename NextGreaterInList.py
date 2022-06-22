from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        # O(n) time and O(n) space complexity
        # O(n) time complexity since the inner while loop at most inserts and pops each element once
        # utilizes a monotonic stack where we go from back to front and add front to back as we go
        
        stack = deque()
        answer = deque()
        
        def helper(curr_node: Optional[ListNode]) -> None:
            if not curr_node.next:
                stack.appendleft(curr_node.val)
                answer.appendleft(0)
                return
            else:
                helper(curr_node.next)
            
            while stack and stack[0] <= curr_node.val:
                stack.popleft()
            
            if stack:
                answer.appendleft(stack[0])
            else:
                answer.appendleft(0)
            
            stack.appendleft(curr_node.val)
        
        helper(head)
        return answer