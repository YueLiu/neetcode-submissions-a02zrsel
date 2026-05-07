class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = []
        ans = 0

        def backtrack(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            return(backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i]))
        
        return backtrack(0,0)

