class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Dict, s2Dict = [0]*26, [0]*26
        for i in range(len(s1)):
            s1Dict[ord(s1[i])-ord('a')] += 1
            s2Dict[ord(s2[i])-ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Dict[i] == s2Dict[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r])-ord('a')
            s2Dict[index] += 1
            if s2Dict[index] == s1Dict[index]:
                matches += 1
            elif s2Dict[index] - 1 == s1Dict[index]:
                matches -= 1
            
            index = ord(s2[l])-ord('a')
            s2Dict[index] -= 1
            if s2Dict[index] == s1Dict[index]:
                matches += 1
            elif s2Dict[index] + 1 == s1Dict[index]:
                matches -= 1
            l += 1
        return matches == 26
