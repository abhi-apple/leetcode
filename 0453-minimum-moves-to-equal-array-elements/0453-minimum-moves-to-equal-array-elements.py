class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mini=min(nums)
        res=0
        for i in nums:
            res=res+i-mini
        return res