class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        zero_positions = []
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    zero_positions.append((i, j))
        
        for i, j in zero_positions:
            for col in range(COLS):
                matrix[i][col] = 0
            for row in range(ROWS):
                matrix[row][j] = 0