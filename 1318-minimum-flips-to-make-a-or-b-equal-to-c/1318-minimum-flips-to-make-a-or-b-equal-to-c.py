class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a=bin(a)[2:]
        b=bin(b)[2:]
        c=bin(c)[2:]
        maxi=max(len(a),len(b),len(c))
        a='0'*(maxi-len(a))+a
        b='0'*(maxi-len(b))+b
        c='0'*(maxi-len(c))+c
        cnt=0
        for i in range(len(c)):
            if c[i]=='0':
                if a[i]=='1' and b[i]=='1':
                    cnt+=2
                elif a[i]=='1' or b[i]=='1':
                    cnt+=1
            if c[i]=='1':
                if a[i]=='0' and b[i]=='0':
                    cnt+=1
        return cnt
                    