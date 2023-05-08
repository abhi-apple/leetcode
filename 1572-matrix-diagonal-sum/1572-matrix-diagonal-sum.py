class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sums = 0
        if len(mat[0]) % 2 == 0:
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if i == j:
                        sums += mat[i][j]
                    elif j == len(mat) - i - 1:
                        sums += mat[i][j]
        else:
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if i == j:
                        sums += mat[i][j]
                    elif i + j == len(mat) - 1:
                        sums += mat[i][j]
      
        return sums
