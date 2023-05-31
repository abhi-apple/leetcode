from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        
        def rec(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
            if i < 0 or j < 0:
                return float('inf')
            if (i,j) in dp :
                return dp[(i,j)]
            
            up = rec(i-1, j)
            left = rec(i, j-1)
            dp[(i,j)] = grid[i][j] + min(up, left)
            return dp[(i,j)]
        
        return rec(len(grid)-1, len(grid[0])-1)
