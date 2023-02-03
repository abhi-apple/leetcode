class Solution:
    def findTargetSumWays(self, nums: List[int], tar: int) -> int:
        tsum=sum(nums)
        n=len(nums)
        if tsum-tar<0:
            return 0
        if (tsum-tar)%2==1:
            return 0
        s2=(tsum-tar)//2
        dp = [[-1 for i in range(s2+1)] for j in range(n)]
        def fres(ind,ta):
            if ind==0:
                if ta==0 and nums[0]==0:
                    return 2
                if ta==0 or ta==nums[0]:
                    return 1
                return 0
            if dp[ind][ta]!=-1:
                return dp[ind][ta]
            nt=fres(ind-1,ta)
            tk=0
            if nums[ind]<=ta:
                tk=fres(ind-1,ta-nums[ind])
            dp[ind][ta]=nt+tk
            return nt+tk
        return fres(n-1,s2)