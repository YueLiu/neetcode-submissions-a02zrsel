class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m, n = len(word1), len(word2)

        dp = [[-1]*(len(word2)+1) for _ in range(len(word1)+1)]


        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i] == word2[j]:
                dp[i][j] = dfs(i+1, j+1)
                return dp[i][j]
            else:
                o_insert = dfs(i, j+1)
                o_delete = dfs(i+1, j)
                o_replace = dfs(i+1, j+1)
                dp[i][j] = min(o_insert, o_delete, o_replace) + 1
                return dp[i][j]
        return dfs(0, 0)
