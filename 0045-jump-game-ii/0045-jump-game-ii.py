class Solution:
    def jump(self, nums: List[int]) -> int:
        res=0
        i=0
        j=0
        while j<len(nums)-1:
            far=0
            for k in range(i,j+1):
                far=max(far,k+nums[k])
            i=j+1
            j=far
            res+=1
        return res