class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l = 0
        r = row*col-1
        while r>=l:
            m = (r+l)>>1
            mrow = m//col
            mcol = m%col
            if matrix[mrow][mcol]==target:
                return True
            elif matrix[mrow][mcol]>target:
                r=m-1
            else:
                l = m+1
        return False
