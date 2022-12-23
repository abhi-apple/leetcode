class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # n=len(prices)
        # dp=[0]*(n+1)
        # dp[0]=0
        # dp[1]=0
        # for i in range(2,n+1):
        #     dp[i]=dp[i-1]
        #     for j in range(0,i-2):
        #         dp[i]=max(dp[i],prices[i-1]-prices[j]+dp[j-2])
        # return dp[n]
        
        dp = {}
        def dfs(i, buyi):
            if i >= len(prices):
                return 0
            if (i, buyi) in dp:
                return dp[(i, buyi)]
            if buyi:
                buy = dfs(i + 1, not buyi) - prices[i]
                coold = dfs(i + 1, buyi)
                dp[(i, buyi)] = max(buy, coold)
            else:
                sell = dfs(i + 2, not buyi) + prices[i]
                coold = dfs(i + 1, buyi)
                dp[(i, buyi)] = max(sell, coold)
            return dp[(i, buyi)]
        return dfs(0, True)

                
                