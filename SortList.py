# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute-force solution: use bubble sort - O(n^2) time and O(1) space
        
#         node = head
#         while node:
#             temp = head
#             swapped = False
#             while temp.next:
#                 prev = temp
#                 next_ = prev.next
                
#                 if prev.val > next_.val:
#                     next_.val, prev.val = prev.val, next_.val
#                     swapped = True
#                 temp = temp.next
            
#             if not swapped:
#                 break
#             node = node.next
#         return head
    
        # merge sort - O(nlogn) time and O(logn) space
        def mergeSort(node: Optional[ListNode]) -> Optional[ListNode]:
            if not head or not node.next:
                return node
                
            # get the midpoint in the linked list
            slow, fast = node, node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            right = slow.next
            slow.next = None
            
            # dividing step
            left_list = mergeSort(node)
            right_list = mergeSort(right)

            # finally merge the sublists
            return merge(left_list, right_list)
            
        def merge(left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
            curr_head = ListNode()
            tail = curr_head
            # iterate over both sublists
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            
            tail.next = left if left else right
            return curr_head.next
        
        return mergeSort(head)