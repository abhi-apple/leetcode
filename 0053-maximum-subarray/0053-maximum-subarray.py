class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        maxi=0
        if len(nums)==1:
            return nums[0]
        for i in nums:
            curr=max(i,curr+i)
            maxi=max(maxi,curr)
        if maxi>0:
            return maxi
        else:
            return max(nums)