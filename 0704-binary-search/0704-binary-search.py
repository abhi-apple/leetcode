class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        i=0
        j=len(nums)-1
        while i<=j:
            mids=(i+j)//2
            if nums[mids]==tar:
                return mids
            elif nums[mids]>tar:
                j=mids-1
            else:
                i=mids+1
        return -1