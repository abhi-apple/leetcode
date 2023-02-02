class Solution:
    def coinChange(self, coins: List[int], am: int) -> int:
        n=len(coins)
        dp=[[-1]*(am+1) for i in range(n)]
        def f(ind,w):
            if ind==0:
                if w%coins[0]==0:
                    return w//coins[0]
                else:
                    return 100000
            if dp[ind][w]!=-1:
                return dp[ind][w]
            nt=f(ind-1,w)
            tk=100000
            if coins[ind]<=w:
                tk=1+f(ind,w-coins[ind])
            dp[ind][w]=min(tk,nt)
            return min(tk,nt)
            
        ans=f(n-1,am)
        if ans>=100000:
            return -1
        
        return ans
            