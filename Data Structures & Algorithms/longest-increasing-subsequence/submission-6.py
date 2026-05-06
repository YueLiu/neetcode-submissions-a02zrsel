class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # top-down
        dp = [1]*(len(nums)+1)

        def dfs(i):
            if dp[i] != 1:
                return dp[i]
            # if i == len(nums):
            #     dp[i] = 0
            #     return 0
            ans = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    ans = max(ans, 1 + dfs(j))
            dp[i] = ans
            return ans
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dfs(i))
        return ans

