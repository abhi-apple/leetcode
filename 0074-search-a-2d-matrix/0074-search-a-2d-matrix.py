class Solution:
    def searchMatrix(self, mat: List[List[int]], tar: int) -> bool:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if tar==mat[i][j]:
                    return True
                if tar<mat[i][j]:
                    return False
        return False