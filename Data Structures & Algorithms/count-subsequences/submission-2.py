class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][len(t)] = 1

        for i in range(len(s)-1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                ans = dp[i+1][j]
                if s[i] == t[j]:
                    ans += dp[i+1][j+1]
                dp[i][j] = ans
        return dp[0][0]
