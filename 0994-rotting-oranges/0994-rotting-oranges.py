class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        que=[]
        vis=[[0 for i in range(m)] for j in range(n)]
        time =0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    que.append([i,j,0])
                    vis[i][j]=2
                else:
                    vis[i][j]=0
        dow=[-1,0,1,0]
        col=[0,1,0,-1]
        
        while que:
            
            r,q,t=que.pop(0)
            time=max(time,t)
            for i in range(4):
                nr=r+dow[i]
                nc=q+col[i]
                if nr>=0 and nr<n and nc>=0 and nc<m and vis[nr][nc]!=2 and grid[nr][nc]==1:
                    que.append([nr,nc,t+1])
                    vis[nr][nc]=2
        for i in range(n):
            for j in range(m):
                if vis[i][j]!=2 and grid[i][j]==1:
                    return -1
        return time
        
            
            