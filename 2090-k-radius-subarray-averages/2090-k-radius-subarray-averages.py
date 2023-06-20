class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[-1]*n
        lw,cuws,dia=0,0,2*k
        for i in range(n):
            cuws+=nums[i]
            if i-lw>=dia:
                res[lw+k]=cuws//(dia+1)
                cuws-=nums[lw]
                lw+=1
        return res
                
                