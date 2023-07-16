class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0]!=0 or grid[n-1][n-1]!=0:
            return -1
        dist=[[float('inf') for i in range(n)] for j in range(n)]
        
        stack=[]
        heapq.heappush(stack,(1,0,0))
        dire=[(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]
        while stack:
            patl,i,j=heapq.heappop(stack)
            if i==n-1 and j==n-1:
                return patl
            for d in dire:
                ix,jx=i+d[0],j+d[1]
                if 0<=ix<n and 0<=jx<n and grid[ix][jx]==0 and patl+1<dist[ix][jx]:
                    dist[ix][jx]=patl+1
                    heapq.heappush(stack,(patl+1,ix,jx))
        return -1
                
                
        