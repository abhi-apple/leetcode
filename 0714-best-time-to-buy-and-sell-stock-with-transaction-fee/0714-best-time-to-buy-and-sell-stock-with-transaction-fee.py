class Solution:
    def maxProfit(self, p: List[int], fee: int) -> int:
        dp={}
        def rec(i,j):
            if i>=len(p):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if j:
                dp[(i,j)]=max(-p[i]+rec(i+1,not j),rec(i+1,j))
            else:
                dp[(i,j)]=max(p[i]-fee+rec(i+1,not j),rec(i+1,j))
            return dp[(i,j)]
        return rec(0,True)