class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n=len(grid)
        dire=[[0,1],[0,-1],[1,0],[-1,0]]
        def inval(r,c):
            return r<0 or c<0 or r==n or c==n
        vis=set()
        def dfs(r,c):
            if inval(r,c) or not grid[r][c] or (r,c) in vis:
                return 
            vis.add((r,c))
            for dr,dc in dire:
                dfs(r+dr,c+dc)
        def bfs():
            res,q=0,deque(vis)
            while q:
                for i in range(len(q)):
                    r,c=q.popleft()
                    for dr,dc in dire:
                        curr,curc=r+dr,c+dc
                        if inval(curr,curc) or (curr,curc) in vis:
                            continue
                        if grid[curr][curc]:
                            return res
                        q.append([curr,curc])
                        vis.add((curr,curc))
                res+=1
            
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()