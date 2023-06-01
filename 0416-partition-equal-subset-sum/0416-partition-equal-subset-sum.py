class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        
        val=sum(nums)//2
        dic={}
        def rec(i,sums):
            if sums==val:
                return True
            if i==len(nums):
                return False
            if (i,sums) in dic:
                return dic[(i,sums)]
            dic[(i,sums)]=rec(i+1,sums) or rec(i+1,sums+nums[i])
            return dic[(i,sums)]
        return rec(0,0)
            