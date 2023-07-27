class Solution:
    def maxRunTime(self, n: int, bat: List[int]) -> int:
        
        i=0
        j=sum(bat)
        ans=0
        def wrk(time):
            whole=0
            for i in range(len(bat)):
                if bat[i]>time:
                    whole+=time
                else:
                    whole+=bat[i]
            return whole>=(time*n)
                    
        while i<=j:
            mid=(i+j)//2
            if wrk(mid):
                i=mid+1
                ans=mid
            else:
                j=mid-1

        return ans
                
                