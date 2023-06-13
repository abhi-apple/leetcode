class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        mat=[]
        cnt=0
        for k in range(len(grid[0])):
            mat.append([row[k] for row in grid])
        # print(mat)
        for i in mat:
            if i in grid:
                cnt+=grid.count(i)
                
        return cnt
        