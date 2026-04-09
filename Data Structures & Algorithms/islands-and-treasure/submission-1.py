class Solution:
    # was Leetcode 286. Walls and Gates
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
 
        from collections import deque

        m, n = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

        # Step 1: Add all treasure chests (0s) as BFS sources
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        # Step 2: BFS outward, filling shortest distance to nearest treasure
        while q:
            r, c = q.popleft()
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                # Only visit INF cells (unvisited land cells)
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1  # distance = parent's distance + 1
                    q.append((nr, nc))
