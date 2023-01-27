class Solution:
    def rob(self, nums: List[int]) -> int:
        pre0=0
        pre1=nums[0]
        for i in range(1,len(nums)):
       
            tk=nums[i] + pre0
            nt=pre1
            pre0=pre1
            pre1=max(tk,nt)
            
        return pre1