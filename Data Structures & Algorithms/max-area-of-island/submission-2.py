class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        maxArea = 0

        def bfs(r, c):
            q = collections.deque()
            area = 1
            q.append((r, c))
            visit.add((r, c))
            while q:
                row, col = q.pop()
                directions = [[1, 0], [0,1] , [-1, 0], [0, -1]]
                for dr, dc in directions:
                    r, c =  dr+row, dc+col
                    if (c in range(cols) and r in range(rows) and grid[r][c] == 1 and (r, c) not in visit):
                        visit.add((r, c))
                        q.append((r,c))
                        area+=1 

            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxArea = max(maxArea, bfs(r, c)) 
                    
        return maxArea