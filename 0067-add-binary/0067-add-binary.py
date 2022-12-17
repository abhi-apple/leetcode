class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=""
        car=0
        if len(a)<len(b):
            a="0"*(len(b)-len(a))+a
        elif len(b)<len(a):
            b="0"*(len(a)-len(b))+b
        for i in range(len(a)-1,-1,-1):
            sums=int(a[i])+int(b[i])+car
            res+=str(sums%2)
            car=sums//2
        if car==1:
            res+="1"
        return res[::-1]
        