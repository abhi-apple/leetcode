from functools import cache

MAX = 10 ** 9 + 7


class Solution:
    def numOfArrays(self, N: int, M: int, K: int) -> int:
        @cache
        def ways(n: int, m: int, k: int) -> int:
            if n * m * k == 0:  # same as: (n == 0 or m == 0 or k == 0)
                return 0
            elif n == k == 1: 
                return 1
            else:
                return (ways(n - 1, m, k) * m +sum(ways(n - 1, mx, k - 1) for mx in range(1, m))) % MAX
        return sum(ways(N, mx, K) for mx in range(1, M + 1)) % MAX