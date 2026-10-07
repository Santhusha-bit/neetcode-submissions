class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rt= 0
        Rb = len(matrix)

        Cl = 0
        Cr = len(matrix[0])

        while Rt < Rb:
            row = (Rt + Rb)//2
            if matrix[row][-1] < target:
                Rt = row + 1
            elif matrix[row][0] > target:
                Rb = row 
            else:
                break
        
        while Cl < Cr:
            m = (Cl+Cr)//2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                Cl = m+1
            else:
                Cr = m
        return False
