class Solution:
    def minDays(self, blom: List[int], m: int, k: int) -> int:
        i=min(blom)
        j=max(blom)
        ans=0
        if len(blom)<m*k:
            return -1
        if len(blom)==m*k:
            return max(blom)
        def rec(val):
            main=0
            cnt=0
            for i in blom:
                
                if val>=i:
                    cnt+=1
                else:
                    if cnt>=k:
                        main+=cnt//k
                    cnt=0
                
            if cnt>=k:
                main+=cnt//k
            
            return main
            
        while i<=j:
            mid=(i+j)//2
            if rec(mid)>=m:
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans