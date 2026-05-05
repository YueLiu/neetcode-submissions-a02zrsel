class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # prefix or suffix trick
        prefix = 1
        suffix = 1
        ans = -2**31
        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[len(nums)-1-i] * (suffix or 1)
            ans = max(ans, max(prefix, suffix))
        return ans
