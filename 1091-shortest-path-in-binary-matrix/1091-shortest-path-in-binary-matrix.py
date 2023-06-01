class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0]==1 or grid[m-1][n-1] == 1:
            return -1
        di = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        que = deque([(0, 0, 1)])  # (i, j, cnt)
        grid[0][0] = 1
        while que:
            i, j, cnt = que.popleft()
            if i == m-1 and j == n-1:
                return cnt
            for p, q in di:
                ni = i + p
                nj = j + q
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                    que.append((ni, nj, cnt+1))
                    grid[ni][nj] = 1
        return -1
