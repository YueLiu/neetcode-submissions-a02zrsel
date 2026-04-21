class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums[0],nums[1])

        dp1 = [0]*(l-1)
        dp2 = [0]*(l-1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0],nums[1])
        for i in range(2,l-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])        
        dp2[0] = nums[1]
        dp2[1] = max(nums[1],nums[2])
        for i in range(2,l-1):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i+1])
        return max(dp1[l-2],dp2[l-2])




        
        