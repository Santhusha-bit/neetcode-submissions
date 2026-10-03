# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = ""
        sum2 = ""
        while l1:
            sum1 += str(l1.val)
            l1 = l1.next

        while l2:
            sum2 += str(l2.val)
            l2 = l2.next
        
        val1 = int(sum1[::-1])
        val2 = int(sum2[::-1])
        val = val1 + val2

        out = str(val)[::-1]

        dummy = ListNode()
        curr = dummy

        for c in out:
            curr.next = ListNode(c)
            curr = curr.next
        
        head = dummy.next

        return head
