class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}
        dp[0] = 1

        for num in nums:
            tmp = {}
            for total, count in dp.items():
                
                if (total + num) not in tmp:
                    tmp[total + num] = count
                else: 
                    tmp[total + num] += count
                if (total - num) not in tmp:
                    tmp[total - num] = count
                else:
                    tmp[total - num] += count
            dp = tmp
        return dp.get(target, 0)