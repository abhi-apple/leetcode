class Solution:
    def numEnclaves(self, mat: List[List[int]]) -> int:
        def dfs(row,col):
            vis[row][col]=1
            n=len(mat)
            m=len(mat[0])
            for i in range(4):
                nr=row+drow[i]
                nc=col+dcol[i]
                if nr>=0 and nr<n and nc>=0 and nc<m and not vis[nr][nc] and mat[nr][nc]==1:
                    dfs(nr,nc)
                    
        n=len(mat)
        m=len(mat[0])
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
        cnt=0
        vis=[[0 for j in range(m)] for i in range(n)]
        
        for j in range(m):
            if not vis[0][j] and mat[0][j]==1:
                dfs(0,j)
            if not vis[n-1][j] and mat[n-1][j]==1:
                dfs(n-1,j)
        
        for i in range(n):
            if not vis[i][0] and mat[i][0]==1:
                dfs(i,0)
            if not vis[i][m-1] and mat[i][m-1]==1:
                dfs(i,m-1)
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and mat[i][j]==1:
                    cnt+=1
        return cnt
                