# class Solution:
#     def containsCycle(self, grid: List[List[str]]) -> bool:
#         vis=set()
#         dire=[(1,0),(0,1),(-1,0),(0,-1)]
#         def dfs(i, j, prev, cur):
            
#             if (i, j) in cur:
#                 return True

#               # Add the current cell to the set before exploring neighbors.

#             for dx, dy in dire:
#                 ix, jx = i + dx, j + dy
#                 print(ix,jx,i,j,prev)
#                 if 0 <= ix < n and 0 <= jx < m and grid[ix][jx] == grid[i][j] and (ix, jx) != prev:
#                     cur.add((i, j))
#                     if dfs(ix, jx, (ix, jx), cur):
#                         return True
#                     cur.remove((i, j))  

#             # Backtrack by removing the current cell from the set.
#             return False

            
            
            
            
#         n=len(grid)
#         m=len(grid[0])
#         for i in range(n):
#             for j in range(m):
#                 if (i,j) not in vis:
#                     if dfs(i,j,(-1,-1),set()):
#                         return True
#         return False



class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]

        def dfs(x, y, prev_x, prev_y, char):
            if visited[x][y]:
                return True

            visited[x][y] = True

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == char and (nx != prev_x or ny != prev_y):
                    if dfs(nx, ny, x, y, char):
                        return True

            return False

        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True

        return False
