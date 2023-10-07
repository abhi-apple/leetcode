from functools import cache

MAX = 10 ** 9 + 7


class Solution:
    def numOfArrays(self, N: int, M: int, K: int) -> int:
        @cache
        def ways(n: int, m: int, k: int) -> int:
            """
            :param n:
            :param m:
            :param k:
            :return: number of ways an array (say A) can be constructed with constraints
                    1) len(A) == n
                    2) max(A) == m
                    3) search_cost(A) = k (definition of search_cost is in problem)
            """
            if n * m * k == 0:  # same as: (n == 0 or m == 0 or k == 0)
                return 0
            elif n == k == 1: 
                return 1
            else:
                return (                    ways(n - 1, m, k) * m

                    +

sum(ways(n - 1, mx, k - 1) for mx in range(1, m))
                ) % MAX
        return sum(ways(N, mx, K) for mx in range(1, M + 1)) % MAX