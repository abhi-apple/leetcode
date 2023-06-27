class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i=1
        j=max(piles)
        def rec(val):
            ans=0
            for k in piles:
                ans+=ceil(k/val)
            return ans
        fin=0
        while i<=j:
            mid=(i+j)//2
            if rec(mid)<=h:
                fin=mid
                j=mid-1
            else:
                i=mid+1
        return fin