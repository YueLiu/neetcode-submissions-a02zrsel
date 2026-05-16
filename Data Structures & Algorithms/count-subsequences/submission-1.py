class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        dp = [[-1]*(len(t)+1) for _ in range(len(s)+1)]

        def dfs(i,j):
            if j == len(t):
                return 1
            if i == len(s) and j < len(t):
                return 0
            if dp[i][j] > -1:
                return dp[i][j]
            ans = dfs(i+1, j)
            if s[i] == t[j]:
                ans += dfs(i+1, j+1)
            dp[i][j] = ans
            return ans
        return dfs(0,0)