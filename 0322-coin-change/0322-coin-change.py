class Solution:
    def coinChange(self, coins: List[int], am: int) -> int:
        dic={}
        n=len(coins)
        def rec(i,m):
            if i==n-1:
                if m%coins[-1]==0:
                    return m//coins[-1]
                else:
                    return float('inf')
            if (i,m) in dic:
                return dic[(i,m)]
            
            nt=rec(i+1,m)
            tk=float('inf')
            if coins[i]<=m:
                tk=1+rec(i,m-coins[i])
            dic[(i,m)]=min(nt,tk)
            return min(nt,tk)
            
        ans=rec(0,am)
        if ans==float('inf'):
            return -1
        return ans
            