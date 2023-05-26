
    
class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        dic = {}

        def rec(i, j):
            if i >= len(mat) or j >= len(mat[0]):
                return 0
            if (i, j) not in dic:
                dwn = rec(i + 1, j)
                rgt = rec(i, j + 1)
                dig = rec(i + 1, j + 1)
                
                dic[(i, j)] = 0
                if mat[i][j] == '1':
                    dic[(i, j)] = min(dwn, rgt, dig) + 1
            return dic[(i, j)]

        rec(0, 0)
        return max(dic.values()) ** 2

                