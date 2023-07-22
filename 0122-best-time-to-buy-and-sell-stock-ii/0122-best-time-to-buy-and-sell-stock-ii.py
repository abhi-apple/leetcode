class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        n=len(prices)
        def rec(i,prev):
            if i==n:
                return 0
            if (i,prev) in dp:
                return dp[(i,prev)]
            if prev:
                dp[(i,prev)]=max(rec(i+1,not prev)+prices[i],rec(i+1,prev))
            else:
                dp[(i,prev)]=max(rec(i+1,not prev)-prices[i],rec(i+1,prev))
            return dp[(i,prev)]
        return rec(0,False)