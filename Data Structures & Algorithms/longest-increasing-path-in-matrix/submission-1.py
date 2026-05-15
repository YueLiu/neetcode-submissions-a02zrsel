class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS, COLS = len(matrix), len(matrix[0])

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        dp = {}

        def dfs(r,c,lastStep):
            if r<0 or c<0 or (r == ROWS) or (c == COLS) or matrix[r][c] <= lastStep:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            res = -1
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                res = max(res, 1 + dfs(nr, nc, matrix[r][c]))
            dp[(r,c)] = res
            return res
        
        ans = -1
        for i in range(ROWS):
            for j in range(COLS):
                ans = max(ans, dfs(i,j,-9999))
        return ans
                