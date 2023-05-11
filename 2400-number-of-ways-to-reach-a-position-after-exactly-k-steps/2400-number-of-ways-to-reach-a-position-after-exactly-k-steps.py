class Solution:
    def numberOfWays(self, st: int, ed: int, k: int) -> int:
        dp=[[-1 for i in range(k+1)] for j in range(3002)]
        def cnt(cur,tar,ki):
            if ki==0 and cur==tar:
                return 1
            if ki==0:
                return 0
            if dp[cur+1000][ki]!=-1:
                return dp[cur+1000][ki]
            a=cnt(cur+1,tar,ki-1)+cnt(cur-1,tar,ki-1)
            dp[cur+1000][ki]=a%(10**9 + 7)
            return dp[cur+1000][ki]
            
        ans=cnt(st,ed,k)
        return ans%(10**9 + 7)