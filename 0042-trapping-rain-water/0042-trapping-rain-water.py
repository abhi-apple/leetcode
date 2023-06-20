class Solution:
    def trap(self, he: List[int]) -> int:
        lft=[]
        mxi=0
        rgt=[]
        for i in range(len(he)):
            lft.append(max(mxi,he[i]))
            mxi=max(he[i],mxi)
        mxi=0
        for i in range(len(he)-1,-1,-1):
            rgt.append(max(mxi,he[i]))
            mxi=max(he[i],mxi)
        rgt=rgt[::-1]
        fin=0
        for i in range(len(he)):
            fin+=min(lft[i],rgt[i])-he[i]
        return fin
            