class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        fir=nums[1:]
        
        s=nums[:-1]
        
        dp1=[0]*len(fir)
        dp2=[0]*len(s)
        dp1[0]=fir[0]
        dp1[1]=max(fir[0],fir[1])
        for i in range(2,len(fir)):
            dp1[i]=max(dp1[i-1],dp1[i-2]+fir[i])
        dp2[0]=s[0]
        dp2[1]=max(s[0],s[1])
        for i in range(2,len(s)):
            dp2[i]=max(dp2[i-1],dp2[i-2]+s[i])
        return max(dp1[-1],dp2[-1])
        