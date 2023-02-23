class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) & 1==1:
            mid=nums[len(nums)//2]
        else:
            mid=(nums[len(nums)//2]+nums[len(nums)//2 -1])//2
        res=0
        for i in nums:
            res=res+abs(i-mid)
        return res
        
        