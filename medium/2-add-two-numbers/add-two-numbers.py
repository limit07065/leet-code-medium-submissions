# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        current = None
        carry_over = 0
        while l1 is not None or l2 is not None:            
            sum = carry_over
            if (l1 is not None):
                sum += l1.val
            if (l2 is not None):
                sum += l2.val
            
            remainder = sum % 10
            if( sum - 10 >= 0):
                carry_over = 1
            else:
                carry_over = 0

            if current is None:     
                head = ListNode(remainder)
                current = head
            else:
                current.next = ListNode(remainder)
                current = current.next
            
            if (l1 is not None):
                l1 = l1.next
            if (l2 is not None):
                l2 = l2.next
        if (carry_over == 1):
            current.next = ListNode(1)
        return head