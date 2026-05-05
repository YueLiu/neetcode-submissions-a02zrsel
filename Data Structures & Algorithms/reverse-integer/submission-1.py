class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        ans = 0
        while x:
            curr = int(math.fmod(x, 10))
            x = int(x/10)
            if ans > int(MAX/10):
                return 0
            if ans == int(MAX/10) and curr > 7:
                return 0
            if ans < int(MIN/10):
                return 0
            if ans == int(MIN/10) and curr < -8:
                return 0

            ans = ans*10 + curr
        return ans