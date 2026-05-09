class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1

        
        def dfs(i, j):
            if i == m-1 and j == n-1:
                return 1
            if i == m or j == n:
                return 0
            if dp[i][j] > 0:
                return dp[i][j]
            ans = dfs(i+1,j) + dfs(i, j+1)
            dp[i][j] = ans
            return ans


        return dfs(0,0)
