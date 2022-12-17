class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for i in nums:
            if original==i:
                original*=2
        return original