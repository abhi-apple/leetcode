class Solution:
    def candy(self, rat: List[int]) -> int:
        n=len(rat)
        data=sorted((x,i) for i,x in enumerate(rat))
        can=[1 for i in range(n)]
        
        for x,i in data:
            if i>0 and rat[i]>rat[i-1]:
                can[i]=max(can[i],can[i-1]+1)
            if i<n-1 and rat[i]>rat[i+1]:
                can[i]=max(can[i],can[i+1]+1)
        return sum(can)
                