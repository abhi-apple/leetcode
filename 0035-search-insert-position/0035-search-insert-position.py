class Solution:
    def searchInsert(self, nums: List[int], tar: int) -> int:
        if tar in nums:
            return nums.index(tar)
        else:
            for i in range(len(nums)):
                if nums[i]>tar:
                    return i
            return len(nums)
            
                
        # i=0
        # j=len(nums)//2
        # while i<j:
        #     if 