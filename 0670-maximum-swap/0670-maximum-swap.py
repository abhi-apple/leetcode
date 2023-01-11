class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        i = 0
        while i < len(nums)-1 and nums[i] >= nums[i+1]:
            i += 1
        if i == len(nums) - 1:
            return num
        k = i
        for j in range(len(nums)-1, i, -1):
            if nums[j] > nums[k]:
                k = j
        for j in range(i+1):
            if nums[j] < nums[k]:
                break
        nums[j], nums[k] = nums[k], nums[j]
        return int(''.join(nums))
#             for j in range(i,len(ans)):
                