class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        mainp = sorted(pairs, key=lambda x: x[1])
        n=len(pairs)
        dp={}
        def rec(i,prev):
            if i==n:
                return 0
            if (i,prev) in dp:
                return dp[(i,prev)]
            nt=rec(i+1,prev)
            tk=0
            if mainp[i][0]>prev:
                tk=rec(i+1,mainp[i][1])+1
            dp[(i,prev)]=max(nt,tk)
            return dp[(i,prev)]
        return rec(0,-float('inf'))