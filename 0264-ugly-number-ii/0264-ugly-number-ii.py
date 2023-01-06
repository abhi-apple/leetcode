class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ug=[1]
        i2=i3=i5=0
        while n>1:
            u2,u3,u5=2*ug[i2],3*ug[i3],5*ug[i5]
            umin=min(u2,u3,u5)
            if umin==u2:
                i2+=1
            if umin==u3:
                i3+=1
            if umin==u5:
                i5+=1
            ug.append(umin)
            n-=1
        return ug[-1]