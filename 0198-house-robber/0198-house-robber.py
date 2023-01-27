class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1 for i in range(len(nums))]
        dp[0]=nums[0]
        neg=0
        for i in range(1,len(nums)):
            if i>1:
                tk=nums[i] + dp[i-2]
            else:
                tk=nums[i]
            nt=dp[i-1]
            dp[i]=max(tk,nt)
        return dp[len(nums)-1]