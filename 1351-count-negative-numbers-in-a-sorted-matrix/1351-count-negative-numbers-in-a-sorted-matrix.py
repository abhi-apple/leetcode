class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt=0
        n=len(grid[0])
        for i in grid:
            for j in range(len(i)):
                if i[j]<0:
                    cnt+=(n-j)
                    break
        return cnt