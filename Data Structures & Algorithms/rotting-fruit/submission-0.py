class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        time = 0

        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh-=1
                        q.append((nr, nc))
            time += 1

        return time if fresh == 0 else -1
            