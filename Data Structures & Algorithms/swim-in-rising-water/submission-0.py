class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        minHeap = [(grid[0][0], 0, 0)] # value, row, column
        visit = set()

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]


        while minHeap:
            val, row, col = heapq.heappop(minHeap)

            if (row, col) in visit:
                continue

            visit.add((row, col))
            
            if row == rows-1 and col == cols-1:
                return val

            for dr, dc in directions:
                r, c = row+dr, col+dc
                if (r in range(rows) and c in range(cols)):
                    heapq.heappush(minHeap, (max(val, grid[r][c]), r, c))

