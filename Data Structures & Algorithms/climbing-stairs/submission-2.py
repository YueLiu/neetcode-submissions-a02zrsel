class Solution:
    def climbStairs(self, n: int) -> int:

        cache = [0] * n

        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] > 0:
                return cache[i]
            ans = dfs(i + 1) + dfs(i + 2)
            cache[i] = ans
            return ans

        return dfs(0)