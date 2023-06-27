class Solution:
    def smallestDivisor(self, nums: List[int], th: int) -> int:
        i=1
        j=max(nums)
        ans=0
        def rec(val):
            res=0
            for i in nums:
                res+=ceil(i/val)
            return res
        while i<=j:
            mid=(i+j)//2
            if rec(mid)<=th:
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans
                
        