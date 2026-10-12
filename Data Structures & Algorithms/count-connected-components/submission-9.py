class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        rank = [1]*n
        
        def find(n1):
            res = n1
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res 

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1

        for n1, n2 in edges:
            n -= union(n1, n2)

        return n
            


        ###### DFS #######
        # nodeToNode = defaultdict(list)

        # for a, b in edges:
        #     nodeToNode[a].append(b)
        #     nodeToNode[b].append(a)

        # visit = set()
        # count = 0

        # def dfs(node):
        #     if node in visit:
        #         return

        #     visit.add(node)

        #     for nei in nodeToNode[node]:
        #         dfs(nei)

        # for i in range(n):
        #     if i not in visit:
        #         dfs(i)
        #         count += 1
            
        # return count

        