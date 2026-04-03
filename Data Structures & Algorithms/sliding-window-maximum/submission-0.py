class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []

        for i in range(len(nums) + 1 - k):
            maxNum = nums[i]
            for j in range(i+1, i+k):
                maxNum = max(maxNum, nums[j])
            ans.append(maxNum)
        return ans
