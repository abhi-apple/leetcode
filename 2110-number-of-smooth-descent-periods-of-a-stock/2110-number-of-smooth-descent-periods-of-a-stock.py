class Solution:
    def getDescentPeriods(self, p: List[int]) -> int:
        dp=[1]*len(p)
        for i in range(1,len(p)):
            if p[i]==p[i-1]-1:
                dp[i]=1+dp[i-1]

        return sum(dp)