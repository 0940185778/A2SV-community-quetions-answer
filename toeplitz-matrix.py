from ast import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])  
        for i in range(rows - 1):
            for j in range(cols - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
    
        return True


matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
print(isToplitzMatrix(matrix)) # type: ignore
