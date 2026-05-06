class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordSet = set(wordDict)
        dp = {len(s):True}

        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(s):
                return True
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordSet:
                    if dfs(j):
                        dp[j] = True
                        return True
            dp[i] = False
            return False

        return dfs(0)