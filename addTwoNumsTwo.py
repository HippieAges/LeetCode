# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from collections import deque
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_stack = deque()
        l2_stack = deque()
        output_stack = deque()
        
        while l1 or l2:
            if l1:
                l1_stack.appendleft(l1.val)
                l1 = l1.next
            if l2:
                l2_stack.appendleft(l2.val)
                l2 = l2.next
            
        longest_stack = l1_stack if len(l1_stack) > len(l2_stack) else l2_stack
        carry = 0
        result = 0
        
        for idx in range(len(longest_stack)):
            if idx < len(l1_stack) and idx < len(l2_stack):
                result = l1_stack[idx] + l2_stack[idx] + carry
            elif idx < len(l1_stack):
                result = l1_stack[idx] + carry
            else: # idx < len(l2_stack)
                result = l2_stack[idx] + carry
            carry = result // 10
            result %= 10
            output_stack.appendleft(result)
        if carry != 0:
            output_stack.appendleft(carry)
        # head = ListNode(output_stack.popleft())
        # temp = head
        
        def recur(output_stack : List[int]) -> Optional[ListNode]:
            if not output_stack:
                return
            
            node = recur(output_stack[1:])
            return ListNode(output_stack[0], node)
            
        return recur(list(output_stack))