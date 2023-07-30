class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def recur(i,j):
            if i == j: return 1
            if dp[i][j] != -1: return dp[i][j]

            min_turn = float('inf')
            for k in range(i,j):
                min_turn = min(min_turn, recur(i,k) + recur(k+1,j))
            
            dp[i][j] = min_turn - int(s[i] == s[j])
            return dp[i][j]
        
        return recur(0,n-1)