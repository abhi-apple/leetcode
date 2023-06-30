class Solution:
    def corpFlightBookings(self, bok: List[List[int]], n: int) -> List[int]:
        val=[0]*(n+1)
        res=[0]*n
        for i in range(len(bok)):
            bok[i]=[bok[i][0]-1,bok[i][1]-1,bok[i][2]]
        for st,ed,cos in bok:
            val[st]+=cos
            val[ed+1]-=cos
        sums=0
        for i in range(n):
            sums+=val[i]
            res[i]=sums
        return res
    
    
