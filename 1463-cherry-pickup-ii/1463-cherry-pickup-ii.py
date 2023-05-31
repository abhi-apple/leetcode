class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dic={}
        def rec(i,j1,j2):
            if j1<0 or j1>=m or j2<0 or j2>=m:
                return float("-inf")
            if i==n-1:
                if j1==j2:
                    return grid[i][j1]
                else:
                    return grid[i][j2]+grid[i][j1]
            if (i,j1,j2) in dic:
                return dic[(i,j1,j2)]
            maxi=0
            for k in [-1,0,1]:
                for p in [-1,0,1]:
                    if j1==j2:
                        maxi=max(maxi,grid[i][j1]+(rec(i+1,j1+k,j2+p)))
                    else:
                        maxi=max(maxi,grid[i][j1]+grid[i][j2]+(rec(i+1,j1+k,j2+p)))
            dic[(i,j1,j2)]=maxi
            return maxi
        return rec(0,0,m-1)