class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))