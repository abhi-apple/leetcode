class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxr=0
        for i ,jum in enumerate(nums):
            print(i,jum)
            if maxr<i:
                return False
            maxr=max(maxr,i+jum)
        return True
    