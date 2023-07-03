class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        mid=0
        hig=len(nums)-1
        while mid<=hig:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
                
                
            elif nums[mid]==1:
                mid+=1
                
                
            elif nums[mid]==2:
                nums[hig],nums[mid]=nums[mid],nums[hig]
                hig-=1
                
                