class Solution:
    def searchInsert(self, nums: List[int], tar: int) -> int:
            
                
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(j+i)//2
            if nums[mid]==tar:
                return mid
            elif nums[mid]>tar:
                j=mid-1
            else:
                i=mid+1
        return i