class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        airportsFromTo = defaultdict(list)

        for f, t in tickets:
            heapq.heappush(airportsFromTo[f], t)

        out= []

        def dfs(airport):
            while airportsFromTo[airport]:
                nextPort = heapq.heappop(airportsFromTo[airport])
                dfs(nextPort)

            out.append(airport)

        dfs("JFK")
        return out[::-1]
            

        