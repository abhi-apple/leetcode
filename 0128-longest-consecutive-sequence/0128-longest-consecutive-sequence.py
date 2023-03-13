class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        cur=1
        if len(nums)==0:
            return 0
        prev=nums[0]
        ans=1
        for i in range(1,len(nums)):
            if nums[i]==prev+1:
       
                cur+=1
            elif nums[i] != prev:
                cur=1
            prev=nums[i]
            ans=max(cur,ans)
        return ans