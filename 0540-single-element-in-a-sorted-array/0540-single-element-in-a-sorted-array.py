class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        for i in range(1,len(nums)-1):
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]
        if nums[-1]!=nums[-2]:
            return nums[-1]
            