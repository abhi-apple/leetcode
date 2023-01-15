from numpy import array
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        mat = array(mat)
        for row1, col1, row2, col2 in queries:
            mat[row1: row2 + 1, col1: col2 + 1] += 1

        return mat