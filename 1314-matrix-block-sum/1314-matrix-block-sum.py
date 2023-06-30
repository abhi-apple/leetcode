from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        res = [[0 for _ in range(m)] for _ in range(n)]

        # Compute the integral image
        integral_image = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                integral_image[i][j] = mat[i][j]
                if i - 1 >= 0:
                    integral_image[i][j] += integral_image[i - 1][j]
                if j - 1 >= 0:
                    integral_image[i][j] += integral_image[i][j - 1]
                if i - 1 >= 0 and j - 1 >= 0:
                    integral_image[i][j] -= integral_image[i - 1][j - 1]

        for i in range(n):
            for j in range(m):
                min_row = max(0, i - k)
                max_row = min(n - 1, i + k)
                min_col = max(0, j - k)
                max_col = min(m - 1, j + k)

                res[i][j] = integral_image[max_row][max_col]

                if min_row > 0:
                    res[i][j] -= integral_image[min_row - 1][max_col]

                if min_col > 0:
                    res[i][j] -= integral_image[max_row][min_col - 1]

                if min_col > 0 and min_row > 0:
                    res[i][j] += integral_image[min_row - 1][min_col - 1]

        return res
