class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows = len(board)
        cols = len(board[0])
        visit = set()

        def dfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))

            while q:
                r, c = q.pop()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr in range(rows) and nc in range(cols) and board[nr][nc] == "O" and (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))
            
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols-1] == "O":
                dfs(r, cols-1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows-1][c] == "O":
                dfs(rows-1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visit:
                    board[r][c] = "X"