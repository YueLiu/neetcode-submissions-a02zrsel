class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        queue = deque()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(ROWS):
            if board[r][0] == 'O':
                queue.append((r,0))
            if board[r][COLS-1] == 'O':
                queue.append((r,COLS-1))            


        for c in range(COLS):
            if board[ROWS-1][c] == 'O':
                queue.append((ROWS-1,c))
            if board[0][c] == 'O':
                queue.append((0,c))   

        while queue:
           r,c = queue.popleft()
           board[r][c] = '2'
           for dr, dc in directions:
                if 0<= r+dr < ROWS and 0 <= c+dc < COLS and board[r+dr][c+dc] == 'O':
                    queue.append((r+dr,c+dc))
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '2':
                    board[r][c] = 'O'
