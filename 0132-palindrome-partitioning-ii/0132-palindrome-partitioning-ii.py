class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = {}
        
        def rec(i):
            if i == n:
                return -1  # Base case: reached the end of the string
            
            if i in dp:
                return dp[i]
            
            cuts = float('inf')
            for j in range(i, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    cuts = min(cuts, 1 + rec(j+1))
            
            dp[i] = cuts
            return dp[i]
        
        return rec(0)
