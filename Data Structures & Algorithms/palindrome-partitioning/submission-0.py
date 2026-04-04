class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        # j: The "Anchor". The start index of our current word.
        # i: The "Scout". The current index we are testing to see if we should make a cut.
        def dfs(j, i):
            
            # 1. BASE CASE: The Scout 'i' has fallen off the end of the string
            if i >= len(s):
                # If j has ALSO reached the end of the string, it means our last 
                # successful cut was perfectly at the end of the word. No letters are leftover!
                if i == j:
                    res.append(part.copy())
                # If j < i, it means we have leftover garbage letters at the end that 
                # didn't form a palindrome. We hit a dead end, so just return and die.
                return

            # 2. DECISION BRANCH A: "Make the Cut"
            # We check if the letters from Anchor (j) to Scout (i) form a palindrome.
            if self.isPali(s, j, i):
                # It is a palindrome! Add this chunk to our path.
                part.append(s[j : i + 1])
                
                # Move BOTH the Anchor and the Scout to the next letter to start a brand new word
                dfs(i + 1, i + 1)
                
                # Backtrack: Remove the chunk so we can try Branch B
                part.pop()

            # 3. DECISION BRANCH B: "Don't Cut (Extend the Word)"
            # Even if we made a cut above, we ALWAYS want to explore what happens 
            # if we didn't cut here. 
            # We keep the Anchor (j) where it is, but move the Scout (i) forward by 1
            # to see if a longer word might also be a palindrome!
            dfs(j, i + 1)

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