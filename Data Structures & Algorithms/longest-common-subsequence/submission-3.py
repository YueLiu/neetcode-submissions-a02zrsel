class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        prev = [0]*(len(text2)+1)

        for i in range(1, len(text1)+1):
            dp = [0]*(len(text2)+1)
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[j] = 1+ prev[j-1]
                else:
                    dp[j] = max(prev[j], dp[j-1])
            prev = dp
        return dp[len(text2)]


