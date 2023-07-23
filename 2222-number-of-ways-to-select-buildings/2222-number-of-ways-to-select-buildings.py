class Solution:
    def numberOfWays(self, s: str) -> int:
        lft=[0]
        rgt=[]
        n=len(s)
        sums=0
        for i in range(n-1):
            sums+=int(s[i])
            lft.append(sums)
        sums=0
        for i in range(n-1,0,-1):
            sums+=int(s[i])
            rgt.append(sums)
        rgt=rgt[::-1]
        rgt.append(0)
        tot=0
        for i in range(1,n-1):
            if s[i]=='0':
                tot+=(lft[i]*rgt[i])
                
            else:
                tot+=((i-lft[i])*((n-i-1)-rgt[i]))
                
        # print(lft,rgt)
        return tot
            