class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=0
        if len(nums)==1:
            return True
        for i in range(len(nums)):
            
            if i>maxi:
                return False
            maxi=max(maxi,i+nums[i])
        return True
            
        