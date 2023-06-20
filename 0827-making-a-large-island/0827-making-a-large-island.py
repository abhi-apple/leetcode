class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid) * len(grid[0])
        par = [i for i in range(n)]
        size = [1] * n
        
        def find(node):
            if par[node] == node:
                return node
            return find(par[node])
        
        def union(i, j):
            pi = find(i)
            pj = find(j)
            if pi == pj:
                return
            if size[pi] > size[pj]:
                par[pj] = pi
                size[pi] += size[pj]
            else:
                par[pi] = pj
                size[pj] += size[pi]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                    for d in dire:
                        ix, jx = i + d[0], j + d[1]
                        if 0 <= ix < len(grid) and 0 <= jx < len(grid[0]) and grid[ix][jx] == 1:
                            main = i * len(grid[0]) + j
                            adj = ix * len(grid[0]) + jx
                            union(main, adj)
                            
        mx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                    ans = set()
                    for d in dire:
                        ix, jx = i + d[0], j + d[1]
                        if 0 <= ix < len(grid) and 0 <= jx < len(grid[0]) and grid[ix][jx] == 1:
                            ans.add(find(ix * len(grid[0]) + jx))
                    siz = 0
                    for k in ans:
                        siz += size[k]
                    mx = max(mx, siz + 1)
        
        return max(mx, max(size))

                    
                    