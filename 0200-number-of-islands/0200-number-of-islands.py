class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        cnt = 0
        
        def bfs(i, j):
            que = [[i, j]]
            vis[i][j] = True
            while que:
                a, b = que.pop(0)
                tpi, tpj = a-1, b
                lfi, lj = a, b-1
                rti, rtj = a, b+1
                bti, btj = a+1, b
                if tpi >= 0 and tpi < len(grid) and tpj >= 0 and tpj < len(grid[0]) and grid[tpi][tpj] == '1' and not vis[tpi][tpj]:
                    que.append([tpi, tpj])
                    vis[tpi][tpj] = True
                if lfi >= 0 and lfi < len(grid) and lj >= 0 and lj < len(grid[0]) and grid[lfi][lj] == '1' and not vis[lfi][lj]:
                    que.append([lfi, lj])
                    vis[lfi][lj] = True
                if rti >= 0 and rti < len(grid) and rtj >= 0 and rtj < len(grid[0]) and grid[rti][rtj] == '1' and not vis[rti][rtj]:
                    que.append([rti, rtj])
                    vis[rti][rtj] = True
                if bti >= 0 and bti < len(grid) and btj >= 0 and btj < len(grid[0]) and grid[bti][btj] == '1' and not vis[bti][btj]:
                    que.append([bti, btj])
                    vis[bti][btj] = True
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not vis[i][j] and grid[i][j] == '1':
                    bfs(i, j)
                    cnt += 1
        return cnt
