class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        res=0
        for i in range(0,n,2):
            res+=nums[i]
        return res