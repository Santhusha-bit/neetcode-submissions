class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodeToNode = defaultdict(list)

        for a, b in edges:
            nodeToNode[a].append(b)
            nodeToNode[b].append(a)

        visit = set()

        def dfs(c, p):
            if c in visit:
                return False

            visit.add(c)

            for nei in nodeToNode[c]:
                if nei == p:
                    continue
                elif not dfs(nei, c):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)

             