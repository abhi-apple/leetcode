from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        vis=set()
        que=deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    que.append((i,j,0))
        while que:
            k=len(que)
            for _ in range(k):
                i,j,tim=que.popleft()
                dire = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                for d in dire:
                    ix,jx=i+d[0],j+d[1]
                    if 0 <= ix < m and 0 <= jx < n:
                        # print(ix,jx,m,n)
                        if mat[ix][jx] == 1 and (ix, jx) not in vis:
                            que.append((ix, jx, tim + 1))
                            ans[ix][jx]=tim+1
                            vis.add((ix, jx))
                                
                                
            

        return ans
            
        
#         def bfs(i, j):
#             vis = set()
#             vis.add((i, j))
#             que = deque([(i, j, 0)])
            
#             while que:
#                 size = len(que)
#                 mini=-float(inf)
                
#                 for _ in range(size):
#                     i, j, tim = que.popleft()
                    
                    
                    
#                     directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#                     for d in directions:
#                         ix, jx = i + d[0], j + d[1]
#                         if 0 <= ix < m and 0 <= jx < n:
#                             if mat[ix][jx] == 1 and (ix, jx) not in vis:
#                                 que.append((ix, jx, tim + 1))
#                                 vis.add((ix, jx))
#                             elif mat[ix][jx] == 0:
#                                 mini=min(mini,tim+1)
#                                 dp[(ix, jx)] = tim + 1
#                                 return tim + 1
#                     dp[(i,j)]=mini
#                     return dp[(i,j)]
#             return 0
        
#         for i in range(m):
#             for j in range(n):
#                 if mat[i][j] == 1:
#                     ans[i][j] = bfs(i, j)
#                     dp[(i, j)] = ans[i][j]
                  
#         return ans

