from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return -1
        dist = [[0 for i in range(n)] for j in range(n)]
        q = deque()
        max_dist = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
        if not q:
            return -1
        while q:
            x, y = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 0:
                    grid[new_x][new_y] = 1
                    q.append((new_x, new_y))
                    dist[new_x][new_y] = dist[x][y] + 1
                    max_dist = dist[new_x][new_y]
        return max_dist