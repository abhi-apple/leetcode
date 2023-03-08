class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        j=1
        for i in range(len(nums)):
            if j==nums[i]:
                j+=1
        return j