class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def an(ar):
            pre0=0
            pre1=ar[0]
            for i in range(1,len(ar)):
                tk=ar[i]+pre0
                nk=pre1
                pre0=pre1
                pre1=max(tk,nk)
            
            return pre1
        
        return max(an(nums[1:]),an(nums[:-1]))
        