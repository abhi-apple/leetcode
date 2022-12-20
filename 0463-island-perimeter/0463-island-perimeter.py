class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri=0
        row=len(grid)
        cols=len(grid[0])
        for i in range(row):
            for j in range(cols):
                if grid[i][j]==1:
                    if i==0 or grid[i-1][j]==0:
                        
                        peri+=1
                        print(peri,"i=0")
                    if i==row-1 or grid[i+1][j]==0:
                        peri+=1
                        print(peri,"i=row")
                    if j==0 or grid[i][j-1]==0:
                        peri+=1
                    if j==cols-1 or grid[i][j+1]==0:
                        peri+=1
                        print(peri,j==cols-1)
        return peri