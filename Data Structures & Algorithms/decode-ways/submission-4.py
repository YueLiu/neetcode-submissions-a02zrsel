class Solution:
    def numDecodings(self, s: str) -> int:
        # bottom-up
        dp1 = 1
        dp2 = 0
        dp_curr = 0

        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                dp_curr = 0
            else:
                dp_curr = dp1
            if (i + 1 < len(s)) and (s[i]=='1' or 
                (s[i] == '2' and s[i+1] in '0123456')):
                dp_curr += dp2
            dp2 = dp1
            dp1 = dp_curr

        return dp_curr