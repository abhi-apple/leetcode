class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(n):
            if n==0:
                return nums[0]
            if n<0:
                return 0
            if dp[n]!=-1:
                return dp[n]
            pic=nums[n]+f(n-2)
            non=f(n-1)
            dp[n]=max(pic,non)
            return dp[n]
        dp=[-1 for i in range(len(nums))]
        return f(len(nums)-1)