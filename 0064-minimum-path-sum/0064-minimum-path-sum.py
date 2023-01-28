class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[1000]*n]*m
        dp[0][0]=grid[0][0]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                else:
                    up=10000
                    dw=10000
                    if i>0:
                        up=min(dp[i-1][j],up)
                    if j>0:
                        dw=min(dp[i][j-1],dw)
                    dp[i][j]=min(up,dw)+grid[i][j]
        return dp[m-1][n-1]
                    