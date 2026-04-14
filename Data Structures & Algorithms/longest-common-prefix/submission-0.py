class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0:
            return ""
        
        ROWS = len(strs)
        COLS = len(strs[0])

        for c in range(0, COLS):
            curr = strs[0][c]
            for r in range(1, ROWS):
                if c == len(strs[r]) or curr != strs[r][c]:
                    return strs[0][0:c]
        return strs[0]