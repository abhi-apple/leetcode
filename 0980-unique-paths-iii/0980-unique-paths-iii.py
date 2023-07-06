class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        zeros = 0
        ans=0
        def backtrack(i, j, count):
            nonlocal ans
            grid[i][j]=3
      

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            total_paths = 0

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != -1 and (ni, nj):
                    if grid[ni][nj]==0:
                        backtrack(ni,nj,count+1)
                    if grid[ni][nj]==2 and count==zeros:
                        ans+=1
                        
            grid[i][j]=0   
            return 

        n = len(grid)
        m = len(grid[0])
        start_i = start_j = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    start_i = i
                    start_j = j
                elif grid[i][j] == 0:
                    zeros += 1

        backtrack(start_i, start_j, 0)
        return ans