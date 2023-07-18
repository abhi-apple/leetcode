class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}
        def rec(i):
            if i in dp:
                return dp[i]
            if i<0:
                return 0
            take=rec(i-2)+nums[i]
            nt=rec(i-1)
            dp[i]=max(take,nt)
            return dp[i]
        return rec(len(nums)-1)