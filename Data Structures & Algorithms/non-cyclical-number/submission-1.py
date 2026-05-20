class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        
        def calculator(n):
            res = 0
            num = str(n)
            for i in range(len(num)):
                res += int(num[i])**2
            return res
        
        while calculator(n) != 1:
            if calculator(n) in seen:
                return False
            else:
                seen.add(calculator(n))
            n = calculator(n)
        return True
