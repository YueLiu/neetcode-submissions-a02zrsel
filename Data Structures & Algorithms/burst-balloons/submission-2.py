class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # bottom-up
        n = len(nums)
        new_nums = [1] + nums + [1]

        dp = [[0]*(n+2) for _ in range(n+2)]

        for l in range(n, 0, -1):
            for r in range(l, n+1):
                for k in range(l, r+1):
                    coins = new_nums[k]*new_nums[l-1]*new_nums[r+1]
                    coins += dp[l][k-1] + dp[k+1][r]
                    dp[l][r] = max(coins, dp[l][r])
        
        return dp[1][n]
