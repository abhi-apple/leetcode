class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp={}
        n=len(stones)
        def rec(i,val):
            if i==n-1:
                return True
            if (i,val) in dp:
                return dp[(i,val)]
            ans=False
            for j in range(i+1,n):
                diff=stones[j]-stones[i]
                if val-1<=diff and val+1>=diff:
                    if rec(j,diff):
                        ans=True
                        break
            dp[(i,val)]=ans
            return dp[(i,val)]
        return rec(0,0)