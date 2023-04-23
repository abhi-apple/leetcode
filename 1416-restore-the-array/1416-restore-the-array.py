class Solution:
    def numberOfArrays(self,s, k):
        N, K, M = len(s), len(str(k)) + 1, 10**9+7
        def valid(s):
            return s[0] != "0" and int(s) <= k
        dp = [0] * K
        for i in range(N-1, -1, -1):
            dp[i%K] = i > N-K and valid(s[i:])
            dp[i%K] = (dp[i%K] + sum(dp[j%K] for j in range(i+1, min(i+K+1, N)) if valid(s[i:j]))) % M
        return dp[0]
