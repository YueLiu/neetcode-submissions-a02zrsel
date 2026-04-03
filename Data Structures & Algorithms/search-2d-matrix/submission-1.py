class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # we are looking for log m*n solution

        rows, cols = len(matrix), len(matrix[0])

        # locate which row contains target, log m 

        lr, rr  = 0, rows - 1

        while lr <= rr:
            mid = lr + ( rr - lr ) // 2
            if (target < matrix[mid][0]) :
                rr = mid - 1
            elif (target > matrix[mid][-1]) :
                lr = mid + 1
            else:
                break
        
        if (lr > rr):
            return False
        row = lr + (rr - lr)//2
        lc, rc = 0, cols - 1

        while lc <= rc:
            mid = lc + ( rc - lc ) // 2
            if (target < matrix[row][mid]) :
                rc = mid - 1
            elif (target > matrix[row][mid]) :
                lc = mid + 1
            else:
                return True
        return False

        
