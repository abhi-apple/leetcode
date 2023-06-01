class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[None] * n for _ in range(n)] for _ in range(n)]

        def rec(r1, c1, c2):
            r2 = r1 + c1 - c2
            if r1 == n or r2 == n or c1 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
            if dp[r1][c1][c2] is not None:
                return dp[r1][c1][c2]
            
            cherries = grid[r1][c1]
            if c1 != c2:
                cherries += grid[r2][c2]

            cherries += max(
                rec(r1, c1 + 1, c2 + 1),
                rec(r1 + 1, c1, c2 + 1),
                rec(r1, c1 + 1, c2),
                rec(r1 + 1, c1, c2)
            )

            dp[r1][c1][c2] = cherries
            return cherries

        return max(0, rec(0, 0, 0))
