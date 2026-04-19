class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        roof = len(cost)

        dp = [0,0]


        for i in range(2,roof+1):
            currStep = min(dp[1]+ cost[i-1], dp[0] + cost[i-2])
            dp[0] = dp[1]
            dp[1] = currStep

        return dp[1]