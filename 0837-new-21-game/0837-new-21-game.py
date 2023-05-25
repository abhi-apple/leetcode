class Solution:
    def new21Game(self, n: int, k: int, maxi: int) -> float:
        if k==0 or n>=k-1+maxi:
            return 1.0
        dp=[0.0]*(n+1)
        prob=0.0
        win=1.0
        dp[0]=1.0
        for i in range(1,n+1):
            dp[i]=win/maxi
            if i<k:
                win+=dp[i]
            else:
                prob+=dp[i]
            if i>=maxi:
                win-=dp[i-maxi]
        return prob