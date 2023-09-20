class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        mini = 1e9
        j = 0
        summ = 0
        if target < 0: return -1 
        for i in range(len(nums)):
            summ+=nums[i]
            while summ > target and j < len(nums):
                summ -= nums[j]
                j+=1
            if summ == target:
                mini = min(mini,(len(nums)- (i-j+1)))
        if mini == 1e9: mini = -1
        return mini