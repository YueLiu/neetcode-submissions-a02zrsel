class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        nums = []
        
        for row in matrix:
            nums += row
        
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l)//2
            if (target < nums[mid]) :
                r = mid - 1
            elif (target > nums[mid]) :
                l = mid + 1
            else:
                return True
        return False