class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)==len(nums)//2:
                return i
        return 1