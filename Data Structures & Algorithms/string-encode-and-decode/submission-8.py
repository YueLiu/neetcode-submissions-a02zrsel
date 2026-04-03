class Solution:

    count = {}

    def encode(self, strs: List[str]) -> str:

        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:

        ans = []
        curr = 0

        while curr < len(s):
            i = curr
            while s[i] != '#':
                i += 1
            length = int(s[curr:i])
            ans.append(s[i+1:i+length+1])
            curr = i + 1 + length
        return ans
