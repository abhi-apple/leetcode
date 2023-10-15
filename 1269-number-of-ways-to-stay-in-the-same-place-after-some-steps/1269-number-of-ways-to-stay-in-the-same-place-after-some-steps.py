class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod=10**9 +7
        dp={}
        def rec(stps,ind):
            if (stps,ind) in dp:
                return dp[(stps,ind)]
            if stps==0:
                return 1 if ind==0 else 0
            if stps<0 or ind<0 or ind>=arrLen:
                return 0
            ways=(rec(stps-1,ind)%mod)
            ways+=(rec(stps-1,ind+1)%mod)
            ways+=(rec(stps-1,ind-1)%mod)
            dp[(stps,ind)]=ways
            return ways
        return rec(steps,0)%mod