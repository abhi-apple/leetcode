class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev=[0]*n
        
        for i in range(m):
            tem=[0]*n
            for j in range(n):
                if i==0 and j==0:
                    tem[j]=1
                else:
                    up=0
                    dw=0
                    if i>0:
                        up=prev[j]
                    if j>0:
                        dw=tem[j-1]
                    tem[j]=up+dw
            prev=tem
        return prev[-1]
                    