class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        # Optimize: 2D Array is infinitely faster than a Dictionary
        # 0 means "Unvisited"
        dp = [[0] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            # If it's not 0, we already calculated the answer!
            if dp[r][c] != 0:
                return dp[r][c]
            
            res = 1 
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check bounds and strictly increasing rule
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1 + dfs(nr, nc))
                    
            # Save the absolute truth
            dp[r][c] = res
            return res
        
        ans = 0
        for i in range(ROWS):
            for j in range(COLS):
                ans = max(ans, dfs(i, j))
                
        return ans
                