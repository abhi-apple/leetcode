class Solution:
    def maxProfit(self, p: List[int]) -> int:
        dp=[[[-1 for i in range(3)] for j in range(2)] for k in range(len(p))]
        def f(ind,buy,cap):
            if cap==0 or ind==len(p):
                return 0
            if dp[ind][buy][cap]!=-1:
                return dp[ind][buy][cap]
            if buy:
                dp[ind][buy][cap]=max(-p[ind]+f(ind+1,0,cap),f(ind+1,1,cap))
                
            else:
                dp[ind][buy][cap]=max(p[ind]+f(ind+1,1,cap-1),f(ind+1,0,cap))
            
            return dp[ind][buy][cap]
            
            
        return f(0,1,2)
        