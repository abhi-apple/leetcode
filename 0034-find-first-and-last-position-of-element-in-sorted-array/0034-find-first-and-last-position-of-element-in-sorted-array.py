class Solution:
    def searchRange(self, nums: List[int], tar: int) -> List[int]:
        i=0
        j=len(nums)-1
        fir=-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==tar:
                fir=mid
                j=mid-1
            elif nums[mid]<tar:
                i=mid+1
            else:
                j=mid-1
        sec=-1
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==tar:
                sec=mid
                i=mid+1
            elif nums[mid]<tar:
                i=mid+1
            else:
                j=mid-1
        return [fir,sec]
        