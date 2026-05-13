class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1)+len(s2):
            return False
        
        prev = [False]*(len(s2)+1)
        prev[len(s2)] = True
        
        for i in range(len(s1), -1, -1):
            dp = [False]*(len(s2)+1)
            if i == len(s1):
                dp = prev
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and prev[j]:
                    dp[j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[j + 1]:
                    dp[j] = True
            prev = dp
        return dp[0]



