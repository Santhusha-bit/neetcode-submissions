"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def clone(old):
            if old in oldToNew:
                return oldToNew[old]

            copy = Node(old.val)
            oldToNew[old] = copy

            for nei in old.neighbors:
                copy.neighbors.append(clone(nei))

            return copy

        return clone(node) if node else None


