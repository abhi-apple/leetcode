class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        n=len(prices)
        def rec(i,bol,cnt):
            if cnt==0 or i==n:
                return 0
            if (i,bol,cnt) in dp:
                return dp[(i,bol,cnt)]
            if bol:
                dp[(i,bol,cnt)]=max(rec(i+1,not bol,cnt-1)+prices[i],rec(i+1,bol,cnt))
            else:
                dp[(i,bol,cnt)]=max(rec(i+1,not bol,cnt)-prices[i],rec(i+1,bol,cnt))
            return dp[(i,bol,cnt)]
        return rec(0,False,2)