class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp={}
        n=len(grid)
        m=len(grid[0])
        
        def rec(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==0 and j==0:
                return grid[0][0]
            if 0>i or i>n-1 or 0>j or j>m-1:
                return float('inf')
            dp[(i,j)]=min(rec(i-1,j),rec(i,j-1))+grid[i][j]
            return dp[(i,j)]
        return rec(n-1,m-1)