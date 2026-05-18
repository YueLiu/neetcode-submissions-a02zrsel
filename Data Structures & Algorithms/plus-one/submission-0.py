class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i]*(10**(len(digits)-1-i))
        num += 1

        ans = [int(n) for n in str(num)]
        return ans
