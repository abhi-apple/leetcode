class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(grid,x,y,ze):
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]==-1:
                return 0
            if grid[x][y]==2:
                return 1 if ze==-1 else 0
            grid[x][y]=-1
            ze-=1
            totp=dfs(grid,x+1,y,ze)+dfs(grid,x,y+1,ze)+dfs(grid,x+-1,y,ze)+dfs(grid,x,y-1,ze)
            grid[x][y]=0
            ze+=1
            return totp
        zero=0
        sx=0
        sy=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    zero+=1
                elif grid[r][c]==1:
                    sx=r
                    sy=c
        return dfs(grid,sx,sy,zero)
    