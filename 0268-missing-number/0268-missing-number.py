class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sums=sum(nums)
        n=len(nums)*(len(nums)+1)/2
        return int(n-sums)