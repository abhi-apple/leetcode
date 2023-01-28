class Solution:
    def minimumTotal(self, tr: List[List[int]]) -> int:
        m = len(tr)
        dp = [0] * (m + 1)
        
        for i in range(m - 1, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + tr[i][j]
        
        return dp[0]
