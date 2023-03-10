class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = n - 2
        l = n - 1
        
        while k >= 0 and nums[k] >= nums[k+1]:
            k -= 1
        
        if k < 0:
            nums.reverse()
        else:
            while nums[k] >= nums[l]:
                l -= 1
            nums[k], nums[l] = nums[l], nums[k]
            nums[k+1:] = reversed(nums[k+1:])