class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        ans = 0

        stack = []

        for i, h in enumerate(heights):
            pointer = i
            while stack and (h < stack[-1][1]):
                ans = max(ans, stack[-1][1]*(i-stack[-1][0]))
                stack.pop()
                pointer -= 1

            stack.append((pointer,h))

        for i, h in stack:
            ans = max(ans, (len(heights)-i)*h)

        return ans