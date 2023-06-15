class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis=set()
        def bfs(i,j):
            vis.add((i,j))
            que=deque([(i,j)])
            cnt=0
            while que:
                dire=[(0,1),(1,0),(0,-1),(-1,0)]
                i,j=que.popleft()
                # print(i,j,grid[i][j])
                cnt+=1
                for d in dire:
                    ix,jx=i+d[0],j+d[1]
                    if 0<=ix<len(grid) and 0<=jx<len(grid[0]) and grid[ix][jx]==1 and (ix,jx) not in vis:
                        # print(ix,jx)
                        vis.add((ix,jx))
                        
                        que.append((ix,jx))
            return cnt
        maxi=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in vis and grid[i][j]==1:
                    maxi=max(maxi,bfs(i,j))
        return maxi
 
    
#         def dfs(i,j):
#             nonlocal fin
#             vis.add((i,j))
#             if i<0 or j<0 or i>len(grid)-1 or j>len(grid)-1:
#                 return 0
#             dire=[(0,1),(1,0),(0,-1),(-1,0)]
            
            
#             # print(i,j,fin)
#             for d in dire:
#                 ix,jx=i+d[0],j+d[1]
#                 if 0<=ix<len(grid) and 0<=jx<len(grid[0]) and grid[ix][jx]==1 and (ix,jx) not in vis:
#                     fin+=1
#                     dfs(ix,jx)
                    
#             return fin