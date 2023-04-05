class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res=0
        maxi=nums[0]
        s=nums[0]
        for i in range (1,len(nums)):
            s+=nums[i]
            if nums[i]>maxi:
                maxi=ceil(s/(i+1))
            res=max(maxi,res)
        return res