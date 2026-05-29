class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = {}
        dp[(m, n)] = True

        def dfs(i, j):
            if j == n:
                return i == m
            if (i, j) in dp:
                return dp[(i, j)]
            match = False
            if i < m and (s[i] == p[j] or p[j] == '.'):
                match = True
            if j < n-1 and p[j+1] == '*':
                dp[(i, j+2)] = dfs(i, j+2) # * as zero
                # dp[(i+1, j)] = False
                if match:
                    dp[(i+1, j)] = dfs(i+1, j) # * as p[j]
                dp[(i, j)] = dp[(i, j+2)] or (match and dp[(i+1, j)])
                return dp[(i, j)]
            if match:
                dp[(i, j)] = dfs(i+1, j+1)
                return dp[(i, j)]
            dp[(i, j)] = False
            return False
        
        return dfs(0,0)

                