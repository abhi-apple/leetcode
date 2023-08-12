class Solution:
    def uniquePathsWithObstacles(self, obj: List[List[int]]) -> int:
        dp={}
        n=len(obj)
        m=len(obj[0])
        if obj[0][0]==1 or obj[n-1][m-1]==1:
            return 0
        def rec(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==0 and j==0:
                return 1
            if 0>i or i>n-1 or 0>j or j>m-1 or obj[i][j]==1:
                return 0
            dp[(i,j)]=rec(i-1,j)+rec(i,j-1)
            return dp[(i,j)]
        return rec(n-1,m-1)
            