class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]

        for t in tokens:
            if t not in operations:
                stack.append(int(t))
            else:
                right = stack.pop()
                left = stack.pop()
                res = self.helper(left, right, t)
                stack.append(res)
        return stack.pop()



    def helper(self, left: int, right: int, t: str) -> int:
        if t == "+":
            return left + right
        elif t == "-":
            return left - right
        elif t == "*":
            return left * right
        elif t == "/":
            return int(left / right)