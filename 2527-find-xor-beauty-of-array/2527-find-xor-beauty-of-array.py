class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            res^=i
        return res