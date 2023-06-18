from typing import List

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        memo = {}
        
        def dfs(i, j):
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            count = 0
            
            for d in dire:
                ix, jx = i + d[0], j + d[1]
                if 0 <= ix < len(grid) and 0 <= jx < len(grid[0]) and grid[ix][jx] > grid[i][j]:
                    count += dfs(ix, jx)
                    count %= int(1e9) + 7
            
            count += 1  # Increment count for the current cell itself
            memo[(i, j)] = count
            return count
        
        total_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total_count += dfs(i, j)
                total_count %= int(1e9) + 7
        
        return total_count

                