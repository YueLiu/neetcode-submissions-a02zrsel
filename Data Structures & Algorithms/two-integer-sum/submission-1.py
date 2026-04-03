# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         ans = {}
#         i = 0
#         for num in nums:
#             if (target - num) in ans:
#                 return[ans[target - num], i]
#             ans[num] = i
#             i += 1

# for i, n in enumerate(nums): is better than use another i
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
      
        for i, num in enumerate(nums):
            if (target - num) in ans:
                return[ans[target - num], i]
            ans[num] = i