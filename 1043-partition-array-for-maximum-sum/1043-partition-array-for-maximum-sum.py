class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp={}
        n=len(arr)
        def rec(i):
            if i==n:
                return 0
            if i in dp:
                return dp[i]
            le=0
            maxi=0
            sums=0
            for p in range(i,min(n,i+k)):
                le+=1
                maxi=max(maxi,arr[p])
                sums=max(maxi*le +rec(p+1),sums)
                
            dp[i]=sums
            return dp[i]
        return rec(0)