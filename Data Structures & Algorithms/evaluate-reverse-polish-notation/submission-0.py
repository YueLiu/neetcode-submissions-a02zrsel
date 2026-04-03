class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]

        for t in tokens:
            if t not in operations:
                stack.append(t)
            else:
                right = stack.pop()
                left = stack.pop()
                res = self.helper(left,right,t)
                stack.append(res)
        return stack[-1]

    def helper(self, left: str, right: str, t: str) -> int:
        if t == "+":
            return int(left) + int(right)
        elif t == "-":
            return int(left) - int(right)
        elif t == "*":
            return int(left) * int(right)
        elif t == "/":
            return int(int(left) / int(right))           