class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans1 = {}
        ans2 = {}
        for i in s:
            if i in ans1:
                ans1[i] += 1
            else:
                ans1[i] = 1
        
        for j in t:
            if j in ans2:
                ans2[j] += 1
            else:
                ans2[j] = 1
        
        if ans1 == ans2:
            return True
        return False