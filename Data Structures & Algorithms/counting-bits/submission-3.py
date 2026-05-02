class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        dp[0] = 0
        floor = 1
        for i in range(1,n+1):
            if i == floor * 2:
                floor = i
            dp[i] = 1 + dp[i - floor]
        return dp