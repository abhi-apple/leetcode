class Solution:
    def shipWithinDays(self, w: List[int], da: int) -> int:
        low=max(w)
        hig=sum(w)
        ans=0
        while low<=hig:
            def istr(mid,da):
                d=1
                sums=0
                for i in range(len(w)):
                    sums+=w[i]
                    if sums>mid:
                        d+=1
                        sums=w[i]
                return True if d<=da else False
            mid=low+(hig-low)//2
            if (istr(mid,da)):
                ans=mid
                hig=mid-1
            else:
                low=mid+1
        return ans
                