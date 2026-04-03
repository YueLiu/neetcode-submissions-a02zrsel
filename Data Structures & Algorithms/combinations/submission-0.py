class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        currComb = []

        def dfs(i):
            if len(currComb) >= k:
                ans.append(currComb.copy())
                return
            if i > n:
                return
            
            # include current value
            currComb.append(i)
            dfs(i+1)
            # not include current value
            currComb.pop()
            dfs(i+1)
        dfs(1)
        return ans