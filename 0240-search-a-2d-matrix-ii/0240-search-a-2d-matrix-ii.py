class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = (m-1)//2
        j = (n-1)//2

        if matrix[i][j] == target:
            return True

        if matrix[i][j] > target:
            if i > 0 and self.searchMatrix(matrix[:i], target):
                return True
            if j > 0 and self.searchMatrix([row[:j] for row in matrix], target):
                return True

        if matrix[i][j] < target:
            if i < m-1 and self.searchMatrix(matrix[i+1:], target):
                return True
            if j < n-1 and self.searchMatrix([row[j+1:] for row in matrix], target):
                return True

        return False
