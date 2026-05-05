class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kadane's
        ans = nums[0]
        currMax = 1
        currMin = 1

        for i in range(len(nums)):
            currMax, currMin = (
            max(currMax*nums[i], nums[i], currMin*nums[i]),
            min(currMin*nums[i], nums[i], currMax*nums[i]))
            ans = max(ans, currMax)
        return ans