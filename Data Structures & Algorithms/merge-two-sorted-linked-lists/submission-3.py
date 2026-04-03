# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val > list2.val:
            out = list2
            tmp1 = list1
            tmp2 = list2.next
        else:
            out = list1
            tmp1 = list1.next
            tmp2 = list2

        #out.next = None
        head = out

        while tmp1 and tmp2:
            if tmp1.val < tmp2.val:
                less = tmp1
                tmp1 = tmp1.next
            else:
                less = tmp2
                tmp2 = tmp2.next

            out.next = less
            out = less

        if tmp1:
            out.next = tmp1
        else:
            out.next = tmp2

        return head