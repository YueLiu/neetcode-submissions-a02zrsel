class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []

        ans = []

        # ( <= N, ) <= N
        def backTracking(openP, closeP):

            if (openP == closeP == n):
                ans.append("".join(stack))
                return
        
            if (openP < n):
                stack.append("(")
                backTracking(openP + 1, closeP)
                stack.pop()
            
            if (closeP < openP):
                stack.append(")")
                backTracking(openP, closeP + 1)
                stack.pop()

        backTracking(0,0)
        return ans

        