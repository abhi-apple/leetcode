class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        dp = {}

        def rec(i, j):
            if i == -1 :
                return j+1
            elif j == -1:
                return i + 1

            if (i, j) in dp:
                return dp[(i, j)]

            if w1[i] == w2[j]:
                dp[(i, j)] = rec(i - 1, j - 1)
                return dp[(i, j)]

            ins = rec(i, j - 1)
            de = rec(i - 1, j)
            rep = rec(i - 1, j - 1)
            dp[(i, j)] = min(ins, de, rep) + 1
            return dp[(i, j)]

        return rec(len(w1) - 1, len(w2) - 1)
