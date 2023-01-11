class Solution:
    def binaryGap(self, n: int) -> int:
        ans=bin(n)
        ans=ans[2:]
        ons=[]
        for i in range(len(ans)):
            if ans[i]=='1':
                ons.append(i)
        maxi=0
        if len(ons)==1:
            return 0
        for i in range(1,len(ons)):
            maxi=max(maxi,ons[i]-ons[i-1])
        return maxi