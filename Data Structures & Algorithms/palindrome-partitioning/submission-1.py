class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(start, end):
            
            # 1. BASE CASE: The Scout 'i' has fallen off the end of the string
            if end == len(s):
                if end == start:
                    res.append(part.copy())
                return

            # 2. DECISION BRANCH A: "Make the Cut"
            if self.isPali(s, start, end):
                part.append(s[start : end + 1])
                dfs(end + 1, end + 1)
                part.pop()

            # 3. DECISION BRANCH B: "Don't Cut (Extend the Word)"
            # Even if we made a cut above, we ALWAYS want to explore what happens 
            # if we didn't cut here. 
            # We keep the Anchor (j) where it is, but move the Scout (i) forward by 1
            # to see if a longer word might also be a palindrome!
            dfs(start, end + 1)

        # Start the recursion with both the Anchor and the Scout at index 0
        dfs(0, 0)
        return res

    # Standard two-pointer palindrome checker
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True