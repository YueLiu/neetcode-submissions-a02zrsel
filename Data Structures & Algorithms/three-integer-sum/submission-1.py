class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = sorted(nums)
        for i, num in enumerate(tmp):
            if num > 0:
                break

            l, r = i + 1, len(tmp) - 1
            target = 0 - num
            while l < r:
                if tmp[l] + tmp[r] == target:
                    res = [num, tmp[l], tmp[r]]
                    if res not in ans:
                        ans.append(res)
                    l += 1
                    r -= 1  # Move both pointers to avoid infinite loop
                elif tmp[l] + tmp[r] < target:
                    l += 1
                else:
                    r -= 1
        return ans
                
