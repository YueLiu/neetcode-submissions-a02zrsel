class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR combination rule
        ans = len(nums)
        for i in range(len(nums)):
            ans ^= i ^ nums[i]
        return ans
