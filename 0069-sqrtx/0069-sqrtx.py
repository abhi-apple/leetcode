class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        j=x
        ans=0
        while i<=j:
            mid=(i+j)//2
            if mid*mid<=x:
                ans= mid
                i=mid+1
            else:
                j=mid-1
        return ans
        