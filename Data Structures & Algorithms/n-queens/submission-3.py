class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if isSafe(r,c,board):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."

        def isSafe(r,c,board):
            row = r - 1
            while row >= 0:
                if board[row][c] == "Q":
                    return False
                row -= 1
            row = r - 1
            col = c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1
            row = r - 1
            col = c + 1
            while row >= 0 and col < len(board):
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            return True


        backtrack(0)
        return res