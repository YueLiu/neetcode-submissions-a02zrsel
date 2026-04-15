class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pac = []
        atl = []

        def dfs(r, c, memo, prevHeight):
            if (r < 0 or c < 0 or [r,c] in memo or r == ROWS or c == COLS or prevHeight > heights[r][c]):
                return
            memo.append([r, c])
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc, memo, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if [r,c] in pac and [r,c] in atl:
                    res.append([r,c])
        return res
             

