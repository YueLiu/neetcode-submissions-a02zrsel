class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        ans = 0
        q = deque()


        def bfs(r,c):
            q.append([r,c])
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    directions = [[1,0],[-1,0],[0,1],[0,-1]]
                    for dr, dc in directions:
                        if (r+dr<0 or c+dc<0 or
                            r+dr >=ROWS or c+dc >= COLS or
                            grid[r+dr][c+dc] == "0"):
                            continue
                        q.append([r+dr,c+dc])
                        grid[r+dr][c+dc]="0"


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    ans += 1
                    bfs(r,c)

        return ans        