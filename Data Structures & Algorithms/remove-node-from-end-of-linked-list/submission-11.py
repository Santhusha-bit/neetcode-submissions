# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = dummy.next

        while n and right:
            right = right.next
            n-=1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next

        # length = 0
        # node= head
        # while node:
        #     length += 1
        #     node = node.next

        # nodeNumber = length - n 
        
        # dummy = ListNode()
        # tail = dummy
        # dummy.next = head

        # for i in range(nodeNumber):
        #     tail = tail.next
        # tail.next = tail.next.next
        # return dummy.next