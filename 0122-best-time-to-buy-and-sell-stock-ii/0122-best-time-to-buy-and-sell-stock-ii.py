class Solution:
    def maxProfit(self, p: List[int]) -> int:
        dp={}
        def rec(i,bol):
            if i==len(p):
                return 0
            if (i,bol) in dp:
                return dp[(i,bol)]
            prof=0
            pr=0
            if bol:
                prof=max(-p[i]+rec(i+1,not bol),rec(i+1,bol))
            else:
                pr=max(rec(i+1,bol),p[i]+rec(i+1,not bol))
            
            dp[(i,bol)]=max(prof,pr)
            return dp[(i,bol)]
        return rec(0,True)