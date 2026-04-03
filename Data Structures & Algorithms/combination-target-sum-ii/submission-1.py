class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        currComb = []
        # currSum = 0

        def dfs(i, currSum):
            if currSum == target:
                ans.append(currComb.copy())
                return
            if i == len(candidates):
                return
            if currSum + candidates[i] > target:
                return
            # include current num
            currComb.append(candidates[i])
            dfs(i+1, currSum + candidates[i])
            currComb.pop()
            # move on to next unique num
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, currSum)
        dfs(0, 0)
        return ans