# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        out = []
        
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = [] 
            for i in range(qLen):
                item = q.popleft()
                if item:
                    level.append(item.val)
                    q.append(item.left)
                    q.append(item.right)
            if level:
                res.append(level)
                out.append(level[-1])

        return out