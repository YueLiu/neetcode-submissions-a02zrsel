class Solution:
    def rob(self, nums: List[int]) -> int:

        def dp(nums):
            r1, r2 = 0, 0
            for num in nums:
                tmp = max(r2, r1+num)
                r1 = r2
                r2 = tmp
            return r2        
        
        return max(nums[0], dp(nums[:-1]), dp(nums[1:]))


