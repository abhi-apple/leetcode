class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        l1=list(s1)
        l2=list(s2)
        l1.sort()
        l2.sort()
        
        a1=0
        a2=0
        for i in range(len(s1)):
            if l1[i]>=l2[i]:
                a1+=1
            if l2[i]>=l1[i]:
                a2+=1
        if a1==len(s1) or a2==len(s1):
            return True
        return False