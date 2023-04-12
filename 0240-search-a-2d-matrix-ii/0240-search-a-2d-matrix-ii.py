class Solution:
    def searchMatrix(self, matrix: List[List[int]], tar: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if tar==matrix[i][j]:
                    return True
        return False