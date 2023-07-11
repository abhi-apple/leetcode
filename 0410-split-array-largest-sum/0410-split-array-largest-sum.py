class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)
        res=r
        def helper(var):
            subar=1
            curs=0
            for n in nums:
                curs+=n
                if curs>var:
                    subar+=1
                    curs=n
            return subar<=k
        while l<=r:
            mid=l+((r-l)//2)
            if helper(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res