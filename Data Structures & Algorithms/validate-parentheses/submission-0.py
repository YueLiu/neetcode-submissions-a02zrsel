class Solution:
    def isValid(self, s: str) -> bool:

        ans = {")": "(", "]": "[", "}": "{"}

        stack = []

        for c in s:
            if c in ans:
                if stack and stack[-1] == ans[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack

        
            