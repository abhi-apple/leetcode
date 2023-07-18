class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        def rec(i):
            if i==0:
                return 1
            if i<0:
                return 0
            if i in dp:
                return dp[i]
            dp[i]=rec(i-1)+rec(i-2)
            return dp[i]
        return rec(n)