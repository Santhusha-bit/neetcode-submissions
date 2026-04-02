# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        node = head
        if node is None:
            return False
        while True:
            node.val = "visited"
            node = node.next
            if node is None:
                return False
            if node.val == "visited":
                return True
            
        

        # Assuming all values are different
        # d = {} 
        # node = head
        # while node:
        #     if node.val in d:
        #         return True
        #     d[node.val] = True
        #     node = node.next
        # return False 