
     
        
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = {}
        
        def rec(i, j):
            if i >= len(matrix) or j >= len(matrix[0]):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = 0
            if matrix[i][j] == 1:
                dwn = rec(i+1, j)
                rgt = rec(i, j+1)
                dig = rec(i+1, j+1)
            
                dp[(i, j)] = min(dwn, rgt, dig) + 1
            return dp[(i, j)]
        
        cnt = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                cnt += rec(i, j)
        
        return cnt

    
                
