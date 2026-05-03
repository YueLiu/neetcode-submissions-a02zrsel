class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {0:0}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            ans = amount + 1
            for coin in coins:
                if i - coin >= 0:
                    ans = min(ans, 1+dfs(i-coin))
                    dp[i] = ans
            return ans
        
        ans = dfs(amount)
        if ans == amount + 1:
            return -1
        else:
            return ans
            
