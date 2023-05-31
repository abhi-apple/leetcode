from typing import List

class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        dic = {}
        ans = []

        def rec(i, j):
            if i == 0 and j>=0 and j<len(mat[0]):
                
                return mat[i][j]
            if i < 0 or j < 0 or  j>=len(mat[0]):
                return float('inf')
            if (i, j) in dic:
                return dic[(i, j)]
         
        
            dic[(i, j)] = mat[i][j] + min(rec(i - 1, j - 1), rec(i - 1, j), rec(i - 1, j + 1))
            return dic[(i, j)]

        for i in range(len(mat[0])):
            ans.append(rec(len(mat) - 1, i))
        return min(ans)
