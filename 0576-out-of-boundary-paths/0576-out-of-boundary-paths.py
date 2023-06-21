class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod=10**9 +7
        dp={}
        def rec(sr,sc,mv):
            if sr<0 or sr>m-1 or sc<0 or sc>n-1:
                return 1
            if mv==0:
                return 0
            if (sr,sc,mv) in dp:
                return dp[(sr,sc,mv)]
            dire=[(0,1),(1,0),(-1,0),(0,-1)]
            cnt=0
            for d in dire:
                ix,jx=sr+d[0],sc+d[1]
                cnt=(cnt+rec(ix,jx,mv-1))%mod
            dp[(sr,sc,mv)]=cnt%mod
            return dp[(sr,sc,mv)]
        return rec(startRow,startColumn,maxMove)%mod