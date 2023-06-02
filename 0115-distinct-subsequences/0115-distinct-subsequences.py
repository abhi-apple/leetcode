class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def rec(i, j):

            if j == 0:
                return 1
            if i == 0:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if s[i - 1] == t[j - 1]:
                dp[(i, j)] = rec(i - 1, j - 1)+rec(i-1,j)
            else:
                dp[(i,j)]=rec(i-1,j)
            return dp[(i, j)]

        return rec(len(s), len(t))
