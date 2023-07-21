class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        x1=[]
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            cnt1=0
            for k in grid[i]:
                if k==1:
                    cnt1+=1
            x1.append(cnt1)
        y1=[]
        for j in range(m):
            cnt=0
            for i in range(n):
                cnt+=grid[i][j]
            y1.append(cnt)
        res=[[0 for i in range(m)] for k in range(n)]
        for i in range(n):
            for j in range(m):
                res[i][j]=(x1[i]+y1[j])-((n-x1[i])+(m-y1[j]))
        return res
        
                    
            