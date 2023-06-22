class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = {}
        
        def rec(i, j):
            if i == -1 or j == -1:
                return ''
            if (i, j) in dp:
                return dp[(i, j)]
            if s1[i] == s2[j]:
                dp[(i, j)] = rec(i - 1, j - 1) + s1[i]
            else:
                tk = rec(i - 1, j)
                ntk = rec(i, j - 1)
                if sum(ord(c) for c in tk) >= sum(ord(c) for c in ntk):
                    dp[(i, j)] = tk
                else:
                    dp[(i, j)] = ntk
            return dp[(i, j)]
        
        ans = rec(len(s1) - 1, len(s2) - 1)
        
        fin = sum(ord(c) for c in s1) + sum(ord(c) for c in s2) - 2 * sum(ord(c) for c in ans)
        return fin

    
            