from functools import cache
from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sums = 0
        def rec(i, mini, maxi):
            nonlocal sums
            if i == len(nums):
                sums += (maxi - mini)
                return
            if mini != float('inf'):
                sums += (maxi - mini)
            rec(i + 1, min(mini, nums[i]), max(maxi, nums[i]))

        for i in range(len(nums)):
            rec(i, float('inf'), -float('inf'))

        return sums
