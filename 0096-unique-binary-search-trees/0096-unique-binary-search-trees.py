class Solution:
    def numTrees(self, n: int) -> int:
        dp=[-1 for i in range(n+1)]
        def solve(n):
            if n<=1:
                return 1
            if dp[n]!=-1:
                return dp[n]
            ans=0
            for i in range(1,n+1):
                ans+=solve(i-1)*solve(n-i)
            dp[n]=ans
            return ans
        
        return solve(n)