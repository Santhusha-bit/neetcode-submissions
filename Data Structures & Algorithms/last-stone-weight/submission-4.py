import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        z = 0
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if y > x:
                z = x - y
            elif x > y:
                z = y - x
            else:
                z=0
            heapq.heappush(stones, z)

        return abs(stones[0])
