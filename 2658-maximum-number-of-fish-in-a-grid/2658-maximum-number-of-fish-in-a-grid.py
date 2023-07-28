class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        maxi=0
        n=len(grid)
        m=len(grid[0])
        
        vis=set()
        def bfs(i,j):
            que=deque()
            que.append((i,j))
            dire=[(0,1),(1,0),(0,-1),(-1,0)]
            cnt=0
            while que:
                
                ip,jp=que.popleft()
                for d in dire:
                    ix,jx=ip+d[0],jp+d[1]
                    if 0<=ix<n and 0<=jx<m and grid[ix][jx]>0 and (ix,jx) not in vis:
                        que.append((ix,jx))
                        vis.add((ix,jx))
                        cnt+=grid[ix][jx]
            
            return cnt
                        
                        
                
            
        for i in range(n):
            for j in range(m):
                if grid[i][j]>0 and (i,j) not in vis:
                    vis.add((i,j))
                    maxi=max(maxi,bfs(i,j)+grid[i][j])
                    
        return maxi
        
        
                
                