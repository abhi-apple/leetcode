class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp={}
        def rec(i,rem):
            if (i,rem) in dp:
                return dp[(i,rem)]
            if rem<=0:
                return 0
            if i==len(cost):
                return float('inf')
            paint=cost[i]+rec(i+1,rem-1-time[i])
            notd=rec(i+1,rem)
            dp[(i,rem)]=min(paint,notd)
            return dp[(i,rem)]
        return rec(0,len(cost))