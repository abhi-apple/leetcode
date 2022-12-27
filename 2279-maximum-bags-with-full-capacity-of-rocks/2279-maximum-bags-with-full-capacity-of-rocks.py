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
        k=0
        while ar>0 and k<len(v):
            if v[k]<=ar:
                c+=1
                ar-=v[k]
            k+=1
        return c