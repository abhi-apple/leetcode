class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        rots=sum(i*nums[i] for i in range(len(nums)))
        elmsum=sum(nums)
        maxrot=rots
        for i in range(len(nums)-1,0,-1):
            rots+=elmsum-len(nums)*nums[i]
            maxrot=max(maxrot,rots)
        return maxrot