class Solution:
    def getSum(self, a: int, b: int) -> int:
        add = a ^ b
        carry = (a & b) << 1

        return add + carry