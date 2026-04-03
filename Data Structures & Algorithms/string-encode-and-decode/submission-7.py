class Solution:

    count = {}

    def encode(self, strs: List[str]) -> str:

        if strs == []:
            return None
    
        ans = ""
        if len(strs) == 0:
            return ans
        self.count = {}
        for i in range(len(strs)):
            self.count[i] = len(strs[i])
            ans += strs[i]
        return ans

    def decode(self, s: str) -> List[str]:

        if s is None:
            return []
        if s == "":
            return [""]

        ans = []
        curr = 0

        for k in list(self.count.values()):
            word = ""
            for i in range(k):
                word += s[curr]
                curr += 1
            ans.append(word)
        return ans
