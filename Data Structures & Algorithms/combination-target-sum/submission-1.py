class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        currComb = []
        currSum = 0

        def dfs(i, currSum):
            if currSum == target:
                ans.append(currComb.copy())
                return
            if currSum > target:
                return
            if i >= len(nums):
                return
            # include current num
            currComb.append(nums[i])
            currSum += nums[i]
            dfs(i, currSum)
            currComb.pop()
            currSum -= nums[i]
            # move on to next num
            dfs(i+1, currSum)
        dfs(0, 0)
        return ans