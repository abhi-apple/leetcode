from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m)]
        
        def rec(i, j):
            if i == 0 and j == 0:
                return 1
            
            if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = rec(i-1, j) + rec(i, j-1)
            return dp[i][j]
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        return rec(m-1, n-1)
