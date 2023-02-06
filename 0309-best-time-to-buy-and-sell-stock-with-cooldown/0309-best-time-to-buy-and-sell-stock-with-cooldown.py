class Solution:
    def maxProfit(self, p: List[int]) -> int:
        dp=[[-1,-1] for j in range(len(p))]
        def f(ind,buy):
            if ind>=len(p):
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            if buy:
                dp[ind][buy]=max(-p[ind]+f(ind+1,0),f(ind+1,1))
            else:
                dp[ind][buy]=max(p[ind]+f(ind+2,1),f(ind+1,0))
            return dp[ind][buy]
            
        return f(0,1)