class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            if tuple(count) in ans:
                ans[tuple(count)].append(s)
            else:
                ans[tuple(count)] = [s]
        
        return ans.values()