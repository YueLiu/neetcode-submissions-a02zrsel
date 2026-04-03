class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[0], height[len(height) - 1]

        while l < r:
            if l_max <= r_max:
                l += 1
                l_max = max(height[l], l_max)
                ans += l_max - height[l]
            else:
                r -= 1
                r_max = max(height[r], r_max)
                ans += r_max - height[r]
                
        return ans
        




                
            
