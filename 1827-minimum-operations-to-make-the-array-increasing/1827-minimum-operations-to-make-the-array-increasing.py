class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                res=res+nums[i-1]-nums[i]+1
                nums[i]=nums[i-1]+1
        return res