class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def dfs(start, currComb):
            # Base Case: We have exactly k numbers
            if len(currComb) == k:
                ans.append(currComb.copy())
                return
                
            # Iterate through all valid NEXT numbers
            for i in range(start, n + 1):
                currComb.append(i)
                dfs(i + 1, currComb)
                currComb.pop()
                
        dfs(1, [])
        return ans