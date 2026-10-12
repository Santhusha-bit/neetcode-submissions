class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodeToNode = defaultdict(list)
        for u, v, t in times:
            nodeToNode[u].append((t, v))

        minHeap = [(0, k)]
        visit = set()
        out = 0

        while minHeap:
            t1, v1 = heapq.heappop(minHeap)
            if v1 in visit:
                continue

            visit.add(v1)
            out = max(t1, out)

            for t2, nei in nodeToNode[v1]:
                if nei not in visit:
                    heapq.heappush(minHeap, (t2 + t1, nei))

        return out if len(visit) == n else -1

                