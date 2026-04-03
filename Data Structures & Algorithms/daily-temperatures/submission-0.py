class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)

        stack = [] # decreasing pair index value

        for i, t in enumerate(temperatures):

            if not stack:
                stack.append([i,t])
            
            while stack and stack[-1][1] < t:
                ans[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            
            stack.append([i,t])
        return ans



