class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        prev = [0]*(amount+1)
        prev[0] = 1

        for i in range(len(coins)):
            dp = [0]*(amount+1)
            dp[0] = 1
            for a in range(amount+1):
                dp[a] = prev[a]
                if a >= coins[i]:
                    dp[a] += dp[a-coins[i]]
            prev = dp
        return prev[amount]