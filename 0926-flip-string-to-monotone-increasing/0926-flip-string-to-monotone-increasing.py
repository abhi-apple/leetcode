class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        oc1=0
        flip=0
        for i in s:
            if i=='1':
                oc1+=1
            else:
                flip=min(flip+1,oc1)
                
        return flip