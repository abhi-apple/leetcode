class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return n-1
        i=1
        j=n-2
        while i<=j:
            mid=(i+j)//2
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]>nums[mid-1]:
                i=mid+1
            else:
                j=mid-1
        return -1
                