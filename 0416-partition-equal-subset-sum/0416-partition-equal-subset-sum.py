class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums=sum(nums)
        if sums &1==1:
            return False
        sums=sums//2
        dp={}
        def rec(i,val):
            if val==sums:
                return True
            if i ==len(nums):
                return False
            if (i,val) in dp:
                return dp[(i,val)]
            dp[(i,val)]=rec(i+1,val) or rec(i+1,val+nums[i])
            return dp[(i,val)]
        return rec(0,0)