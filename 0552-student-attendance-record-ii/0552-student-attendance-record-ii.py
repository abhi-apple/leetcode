class Solution:
    def checkRecord(self, n: int) -> int:
        @lru_cache(maxsize=256)
        def rec(i,a,l):
            if i==n:
                return 1
            res=0
            res+=rec(i+1,a,0)
            if a<1:
                res+=rec(i+1,1,0)
            if l<2:
                res+=rec(i+1,a,l+1)
            return res%(10**9 +7)
        return rec(0,0,0)
        