class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans=[]
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return nums[i]