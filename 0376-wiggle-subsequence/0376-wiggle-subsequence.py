class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ev=1
        od=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                ev=od+1
            elif nums[i]<nums[i-1]:
                od=ev+1
        return max(ev,od)