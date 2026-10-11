class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        area=0

        def dfs(r, c):
            if (r<0 or r==rows or c<0 or c==cols or grid[r][c] == 0 or (r,c) in visit):
                return 0

            visit.add((r, c))
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))

        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
                
        return area














        # if not grid:
        #     return 0

        # rows = len(grid)
        # cols = len(grid[0])
        # visit = set()
        # maxArea = 0

        # def bfs(r, c):
        #     q = collections.deque()
        #     area = 1
        #     q.append((r, c))
        #     visit.add((r, c))
        #     while q:
        #         row, col = q.popleft()
        #         directions = [[1, 0], [0,1] , [-1, 0], [0, -1]]
        #         for dr, dc in directions:
        #             r, c =  dr+row, dc+col
        #             if (c in range(cols) and r in range(rows) and grid[r][c] == 1 and (r, c) not in visit):
        #                 visit.add((r, c))
        #                 q.append((r,c))
        #                 area+=1 

        #    return area


        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1 and (r, c) not in visit:
        #             maxArea = max(maxArea, bfs(r, c)) 
                    
        # return maxArea