class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0]*len(temperatures)

        stack = [] # monotonically decreasing order

        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                ans[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append([i,v])

        return ans