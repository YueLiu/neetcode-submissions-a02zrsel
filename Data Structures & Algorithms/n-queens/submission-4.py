class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        verticalSet = set()
        leftTop = set()
        rightTop = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c not in verticalSet and (r - c) not in leftTop and (r + c) not in rightTop:
                    board[r][c] = "Q"
                    verticalSet.add(c)
                    leftTop.add(r-c)
                    rightTop.add(r+c)
                    backtrack(r + 1)
                    board[r][c] = "."
                    verticalSet.remove(c)
                    leftTop.remove(r-c)
                    rightTop.remove(r+c)


        backtrack(0)
        return res