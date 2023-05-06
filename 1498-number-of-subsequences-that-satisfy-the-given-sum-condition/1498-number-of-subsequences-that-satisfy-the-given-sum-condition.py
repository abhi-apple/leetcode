class Solution:
    def numSubseq(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=0
        MOD=(10**9 + 7)
        r=len(nums)-1
        for i,l in enumerate(nums):
            while (l+nums[r])>k and i<=r:
                r-=1
            if i<=r:
                res+=(2**(r-i))
                res=res%MOD
                
                
                
        
        return res