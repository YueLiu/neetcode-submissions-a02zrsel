class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def backtrack(i, total):
            if i == len(nums):
                if total == target:
                    dp[(i,total)] = 1
                    return 1
                else:
                    return 0
            if (i,total) in dp:
                return dp[(i,total)]
            ans = backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])
            dp[(i,total)] = ans
            return ans
        
        return backtrack(0,0)

