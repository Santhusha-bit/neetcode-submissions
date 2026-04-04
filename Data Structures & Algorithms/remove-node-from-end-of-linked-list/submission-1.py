# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        length = 0
        node= head
        while node:
            length += 1
            node = node.next
        
        nodeNumber = length - n 
        
        dummy = ListNode()
        tail = dummy
        dummy.next = head

        for i in range(nodeNumber):
            tail = tail.next
        try:
            tail.next = tail.next.next
        except:
            return None
        return dummy.next