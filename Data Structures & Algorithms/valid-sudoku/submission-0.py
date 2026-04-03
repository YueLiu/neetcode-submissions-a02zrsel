class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r]):
                    return False;
                rows[r].add(board[r][c])
                if (board[r][c] in cols[c]):
                    return False;
                cols[c].add(board[r][c])
                if (board[r][c] in squares[(int(r/3), int(c/3))]):
                    return False;
                squares[(int(r/3), int(c/3))].add(board[r][c])
        return True
                
