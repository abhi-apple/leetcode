class Solution:
    def trap(self, he: List[int]) -> int:
        if not he: return 0
        l,r=0,len(he)-1
        lm,rm=he[l],he[r]
        res=0
        while l<r:
            if lm<rm:
                l+=1
                lm=max(lm,he[l])
                res+=lm-he[l]
            else:
                r-=1
                rm=max(rm,he[r])
                res+=rm-he[r]
        return res