class Solution:
    def maxProfit(self, p: List[int]) -> int:
        prof=0
        def ans(ind,buy):
            if ind==len(p):
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            if buy:
                dp[ind][buy]=max(-p[ind]+ans(ind+1,0),ans(ind+1,1))
                
            else:
                dp[ind][buy]=max(p[ind]+ans(ind+1,1),ans(ind+1,0))
      
            return dp[ind][buy]
                
            
            
        dp=[[-1,-1] for i in range(len(p))]
        return ans(0,1)
        