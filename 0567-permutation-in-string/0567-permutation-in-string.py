class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=list(s1)
        l1.sort()
        l2=list(s2)
        i=0
        j=len(l1)-1
        while j<len(s2):
            com=l2[i:j+1]
            com.sort()
            if l1==com:
                return True
            i+=1
            j+=1
        return False
        