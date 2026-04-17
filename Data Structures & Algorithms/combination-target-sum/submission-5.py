class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort()
        ans = []

        def dfs(i, currCom, currSum):
            if currSum == target:
                ans.append(currCom.copy())
                return
            if currSum > target:
                return
            if i == len(nums):
                return
            currCom.append(nums[i])
            currSum += nums[i]
            dfs(i, currCom, currSum)
            currCom.pop()
            currSum -= nums[i]
            dfs(i+1, currCom, currSum)

        dfs(0,[],0)
        return ans
                



