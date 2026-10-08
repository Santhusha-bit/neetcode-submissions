# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(curr):
            if not curr:
                return None
            if curr == q or curr == p:
                return curr
            right = dfs(curr.right)

            left = dfs(curr.left)

            if left and right:
                return curr

            return left if left else right


        return dfs(root)
        