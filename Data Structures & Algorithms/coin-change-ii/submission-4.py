class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # Just ONE array!
        dp = [0] * (amount + 1)
        dp[0] = 1 # Base case

        for coin in coins:
            # We start at the coin's value, because anything smaller than the 
            # coin obviously can't use it, so the value stays exactly the same!
            for a in range(coin, amount + 1):
                
                # dp[a] automatically acts as "prev[a]" until we add to it!
                dp[a] += dp[a - coin]
                
        return dp[amount]