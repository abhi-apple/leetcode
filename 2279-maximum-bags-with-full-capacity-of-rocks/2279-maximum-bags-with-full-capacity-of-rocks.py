class Solution:
    def maximumBags(self, cap: List[int], rocks: List[int], ar: int) -> int:
        v=[]
        c=0
        
        for i in range(len(rocks)):
            p=cap[i]-rocks[i]
            if p>0:
                v.append(p)
            else:
                c+=1
        v.sort()
        res=0
        for i in v:
            if i<=ar:
                c+=1
                ar-=i
        return c