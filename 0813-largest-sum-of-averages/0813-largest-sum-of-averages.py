class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n=len(nums)
        dp={}
        def rec(i,cnt):
            if i>=n or cnt==0:
                return float(0)
            if cnt==1:
                return sum(nums[i:])/(n-i)
            if (i,cnt) in dp:
                return dp[(i,cnt)]
            maxi=0
            tot=0
            for ix in range(i,n):
                tot+=nums[ix]
                avg=tot/(ix-i+1)
                maxi=max(maxi,avg+rec(ix+1,cnt-1))
        
            dp[(i,cnt)]=maxi
            return dp[(i,cnt)]
        return rec(0,k)
            