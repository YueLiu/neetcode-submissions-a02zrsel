class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = False
        dp = {}

        def dfs(i, hold):
            if i >= len(prices):
                return 0
            if (i, hold) in dp:
                return dp[(i, hold)]
            skip = dfs(i+1, hold)
            if hold:
                sell = dfs(i+2, not hold) + prices[i]
                dp[(i, hold)] = max(sell, skip)
            if not hold:
                buy = dfs(i+1, not hold) - prices[i]
                dp[(i, hold)] = max(buy, skip)
            return dp[(i, hold)]

        return dfs(0, False)
            