

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         cnt=0
#         vis=set()
#         def dfs(i,j):
#             vis.add((i,j))
#             dire = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#             for d in dire:
#                 ix,jx=i+d[0],j+d[1]
#                 if 0<=ix<len(grid) and 0<=jx<len(grid[0]) and (ix,jx) not in vis and grid[ix][jx]=='1':
#                     dfs(ix,jx)
                
        
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if (i,j) not in vis and grid[i][j]=='1':
#                     dfs(i,j)
#                     # print(cnt)
#                     cnt+=1
#         return cnt
                    
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        vis = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def bfs(i, j):
            vis.add((i, j))
            que = deque([(i, j)])
            while que:
                n, p = que.popleft()
                for d in directions:
                    nx, px = n + d[0], p + d[1]
                    if (nx, px) not in vis and 0 <= nx < len(grid) and 0 <= px < len(grid[0]) and grid[nx][px] == '1':
                        que.append((nx, px))
                        vis.add((nx, px))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in vis and grid[i][j] == '1':
                    bfs(i, j)
                    cnt += 1
        return cnt
