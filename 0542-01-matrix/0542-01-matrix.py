class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        vis=[[1 for i in range(m)] for j in range(n)]
        dist=[[1 for i in range(m)] for j in range(n)]
        que=[]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    que.append([i,j,0])
                    vis[i][j]=0
                else:
                    vis[i][j]=1
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
        
        while que:
            row,col,step=que.pop(0)
            dist[row][col]=step
            for i in range(4):
                nrow=row+drow[i]
                ncol=col+dcol[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and vis[nrow][ncol]==1:
                    vis[nrow][ncol]=0
                    que.append([nrow,ncol,step+1])
                    
        return dist
            