class Solution:
    def maxScore(self, nums: List[int]) -> int:
        dp=[-1 for i in range(1<<14)]
        m=len(nums)
        n=m//2
        def rec(op,mask,dp):
            if op>n:
                return 0
            if dp[mask]!=-1:
                return dp[mask]
            for i in range(m):
                if mask & 1<<i:
                    continue
                for j in range(i+1,m):
                    if mask & 1<<j :
                        continue
                    newm=(1<<i) | (1<<j) | mask
                    sc=op * gcd(nums[i],nums[j])+rec(op+1,newm,dp)
                    dp[mask]=max(dp[mask],sc)
            return dp[mask]
        return rec(1,0,dp)