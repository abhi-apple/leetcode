class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums=[-float('inf')]+nums
        nums.append(-float('inf'))
        for i in range(len(nums)):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i-1
        