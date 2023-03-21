class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res=[]
        j=0
        for i in range(len(nums)):
            if nums[i]==0:
                j+=1
            else:
                res.append(j)
                j=0
                
        if nums[-1]==0:
            res.append(j)
        ans=0
        for i in res:
            ans+=(i*(i+1))//2
        return ans
               