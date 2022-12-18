class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        result = 0

        # Iterate through each building in the grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # Find the maximum height of the buildings in the same row and same column as the current building
                max_row = max(grid[r])
                max_col = max([grid[i][c] for i in range(len(grid))])

                # Calculate the difference between the maximum height and the current building's height
                diff = min(max_row, max_col) - grid[r][c]

                # Add this difference to the result
                result += diff

        # Return the result
        return result