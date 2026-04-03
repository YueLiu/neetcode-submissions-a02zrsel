class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        ans = 0

        l, r = 0, len(heights) - 1

        while l < r:
            ans = max(ans, min(heights[l], heights[r])*(r-l))
            if heights[l] <= heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
        return ans
