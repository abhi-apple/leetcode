class Solution:
    def sumGame(self, num: str) -> bool:
        lfts=0
        lftc=0
        n=len(num)
        for i in range(n//2):
            if num[i]=='?':
                lftc+=1
            else:
                lfts+=int(num[i])
        rgtc=0
        rgts=0
        for i in range(n//2,n):
            if num[i]=='?':
                rgtc+=1
            else:
                rgts+=int(num[i])
        finals=lfts-rgts
        finalc=rgtc-lftc
        # print(finals,finalc)
        return not (finalc & 1==0 and (finalc //2)*9==finals )