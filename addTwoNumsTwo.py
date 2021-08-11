# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # first we need to figure which list is longer 
        l1_len, l2_len = 0, 0
        l1_temp, l2_temp = l1, l2
        while l1_temp or l2_temp:
            if l1_temp:
                l1_len += 1
                l1_temp = l1_temp.next
            if l2_temp:
                l2_len += 1
                l2_temp = l2_temp.next
        
        # then add the two lists together, not worrying about carry for now
        l1_temp, l2_temp = l1, l2
        l1_longest, l2_longest = False, False
        longer_len = 0
        prev = None
        
        if l1_len > l2_len:
            longer_len = l1_len
            l1_longest = True
        else:
            longer_len = l2_len
            l2_longest = True
        
        for _ in range(longer_len):
            if l1_len > l2_len:
                l1_len -= 1
                l1_temp.next, prev, l1_temp = prev, l1_temp, l1_temp.next
            elif l2_len > l1_len:
                l2_len -= 1
                l2_temp.next, prev, l2_temp = prev, l2_temp, l2_temp.next
            else: # l1_len == l2_len
                if l1_longest:
                    l1_temp.val = l1_temp.val + l2_temp.val
                    l1_temp.next, prev, l1_temp = prev, l1_temp, l1_temp.next
                    l2_temp = l2_temp.next
                elif l2_longest:
                    l2_temp.val = l1_temp.val + l2_temp.val
                    l2_temp.next, prev, l2_temp = prev, l2_temp, l2_temp.next
                    l1_temp = l1_temp.next
        
        # finally deal with carry and reverse the list back to its original place
        curr = prev
        prev = None
        carry = 0
        
        while curr:
            curr.val += carry
            carry, value = divmod(curr.val, 10)
            curr.val = value
            curr.next, prev, curr = prev, curr, curr.next 
        if carry != 0:
            node = ListNode(carry, prev)
            prev = node
        return prev