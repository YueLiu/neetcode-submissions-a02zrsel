class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(start, end):
            if end >= len(s):
                if start == end:
                    res.append(part.copy())
                return

            if self.isPali(s, start, end):
                part.append(s[start: end + 1])
                dfs(end+1, end+1)
                part.pop()
            dfs(start, end+1)
        
        dfs(0,0)
        return res

    # Standard two-pointer palindrome checker
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True
