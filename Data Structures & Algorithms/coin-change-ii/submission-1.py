class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = {}

        def dfs(i, amount):
            if amount == 0:
                dp[(i,0)] = 1
                return 1
            if i == len(coins):
                return 0
            if (i, amount) in dp:
                return dp[(i,amount)]

            ans = dfs(i+1, amount)
            if amount >= coins[i]:
                ans += dfs(i, amount-coins[i])
            dp[(i,amount)] = ans
            return ans

        return dfs(0,amount)