class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodeToNode = defaultdict(list)

        for a, b in edges:
            nodeToNode[a].append(b)
            nodeToNode[b].append(a)

        visit = set()
        count = 0

        def dfs(node):
            if node in visit:
                return

            visit.add(node)

            for nei in nodeToNode[node]:
                dfs(nei)

        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
            
        return count

        