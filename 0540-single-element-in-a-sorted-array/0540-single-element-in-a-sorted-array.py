class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        j=len(nums)-1
        if j==0:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
        i=1
        j-=1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if (mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1]):
                i=mid+1
            else:
                j=mid-1
        