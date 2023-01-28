class Solution:
    def uniquePathsWithObstacles(self, obg: List[List[int]]) -> int:
        dp=[[0]*len(obg[0])]*len(obg)
        dp[0][0]=1
        if obg[0][0]==1 or obg[len(obg)-1][len(obg[0])-1]==1:
            return 0
        for i in range(len(obg)):
            for j in range(len(obg[0])):
                if i==0 and j==0:
                    continue
                elif obg[i][j]!=1:
                    up=0
                    dw=0
                    if i>0 and obg[i-1][j]!=1:
                        up=dp[i-1][j]
                    if j>0 and obg[i][j-1]!=1:
                        dw=dp[i][j-1] 
                    dp[i][j]=up+dw
        return dp[len(obg)-1][len(obg[0])-1]
                    
        