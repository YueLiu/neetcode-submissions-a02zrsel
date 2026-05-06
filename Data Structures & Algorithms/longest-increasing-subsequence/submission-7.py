class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bottom-up
        dp = [1]* len(nums)
        res = 1
        for i in range(len(nums)-1, -1, -1):
            ans = 1
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    ans = max(ans, 1+dp[j])
            dp[i] = ans
            res = max(res, dp[i])
        return res
            