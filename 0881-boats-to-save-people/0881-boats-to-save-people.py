class Solution:
    def numRescueBoats(self, pep: List[int], limit: int) -> int:
        pep.sort()
        l=0
        ans=0
        r=len(pep)-1
        while l<=r:
            if pep[l]+pep[r]<=limit:
                l+=1
                r-=1
                ans+=1
            else:
                r-=1
                ans+=1
        return ans