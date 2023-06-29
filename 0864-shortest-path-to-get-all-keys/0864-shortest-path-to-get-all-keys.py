import collections

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        cnt = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    start = [r, c]
                if grid[r][c] in 'abcdef':
                    cnt += 1

        queue = collections.deque([(start[0], start[1], '')])
        seen = set()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        steps = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                x, y, key = queue.popleft()
                if len(key) == cnt:
                    return steps

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
                        cell = grid[nx][ny]
                        if cell in 'ABCDEF' and cell.lower() not in key:
                            continue
                        new_key = key
                        if cell in 'abcdef' and cell not in new_key:
                            new_key += cell
                        if (nx, ny, new_key) not in seen:
                            seen.add((nx, ny, new_key))
                            queue.append((nx, ny, new_key))

            steps += 1

        return -1
