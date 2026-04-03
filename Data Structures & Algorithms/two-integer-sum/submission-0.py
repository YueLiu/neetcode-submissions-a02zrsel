class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        i = 0
        for num in nums:
            if (target - num) in ans:
                return[ans[target - num], i]
            ans[num] = i
            i += 1

        