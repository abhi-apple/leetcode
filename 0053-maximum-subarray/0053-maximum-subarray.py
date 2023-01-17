class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums=0
        maxi=-10000
        for i in nums:
            sums+=i
            maxi=max(sums,maxi)
            if sums<0:
                sums=0
        return maxi