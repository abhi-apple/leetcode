
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = {}

        def rec(i, j):
            if i > n - 1 and j > m - 1:
                return True
            if j > m - 1:
                return False

            if (i, j) in dp:
                return dp[(i, j)]

            if j != m - 1 and p[j + 1] == '*':
                if i < n and (p[j] == s[i] or p[j] == '.'):
                    dp[(i, j)] = rec(i + 1, j) or rec(i, j + 2)
                else:
                    dp[(i, j)] = rec(i, j + 2)
            elif i < n and (p[j] == s[i] or p[j] == '.'):
                dp[(i, j)] = rec(i + 1, j + 1)
            else:
                dp[(i, j)] = False

            return dp[(i, j)]

        return rec(0, 0)

                
            