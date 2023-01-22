class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        sums = 0
        for i in range(32):
            on = 0
            for j in range(len(nums)):
                if (nums[j] & (1 << i)) > 0:
                    on += 1
            sums += on * (len(nums) - on)
        return sums