class Solution:
    def bestClosingTime(self, cus: str) -> int:
        clsl=[]
        cnt=0
        for i in cus:
            if i=='N':
                cnt+=1
            clsl.append(cnt)
        clsr=[]
        cnt=0
        for i in cus[::-1]:
            if i=='Y':
                cnt+=1
            clsr.append(cnt)
        clsr=clsr[::-1]
        clsr.append(0)
        clsl=[0]+clsl
        ind=0
        mini=float('inf')
        for i in range(len(clsr)):
            sums=clsr[i]+clsl[i]
            if sums<mini:
                ind=i
                mini=sums
                
        return ind
            