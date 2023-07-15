# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         n=len(mat)
#         m=len(mat[0])
#         res=[[0 for i in range(m)] for j in range(n)]
#         stack=deque()
#         for i in range(n):
#             for j in range(m):
#                 if mat[i][j]==0:
#                     stack.append((i,j))
#         cnt=1
#         dire=[(0,1),(1,0),(-1,0),(0,-1)]
#         # vis=set()
#         while stack:
#             n=len(stack)
#             for _ in range(n):
#                 i,j=stack.popleft()
#                 for d in dire:
#                     ix,jx=i+d[0],j+d[1]
#                     print(ix,jx)
#                     if 0<=ix<n and 0<=jx<m and mat[ix][jx]==1:
#                         res[ix][jx]=cnt
#                         mat[ix][jx]=0
#                         stack.append((ix,jx))
#         return mat
                
            
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        res = [[0 for _ in range(m)] for _ in range(n)]
        stack = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    stack.append((i, j))
        cnt = 1
        dire = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while stack:
            size = len(stack)
            for _ in range(size):
                i, j = stack.popleft()
                for d in dire:
                    ix, jx = i + d[0], j + d[1]
                    if 0 <= ix < n and 0 <= jx < m and mat[ix][jx] == 1:
                        res[ix][jx] = cnt
                        mat[ix][jx] = 0
                        stack.append((ix, jx))
            cnt += 1
        return res
