class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        cache = {}

        def dfs(i):
            if i == 0:
                return cost[0]
            if i == 1 :
                return cost[1]
            if i in cache:
                return cache[i]

            cache[i] = cost[i] + min(dfs(i-1), dfs(i-2))
            
            return cache[i]

        return min(dfs(len(cost) - 1), dfs(len(cost) - 2))
        