class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=list(s1)
        l2=list(s2)
        j=len(l1)-1
        dicl1={}
        for i in l1:
            if i in dicl1:
                dicl1[i]+=1
            else:
                dicl1[i]=1
        
        dictl2=Counter(l2[:len(l1)])
        i=0
        j=len(l1)-1
        while j<len(l2):
            if dictl2==dicl1:
                return True
            else:
                dictl2[l2[i]]-=1
                if dictl2[l2[i]]==0:
                    del dictl2[l2[i]]
                i+=1
                j+=1
                if j<len(l2):
                    if l2[j] in dictl2:
                        dictl2[l2[j]]+=1
                    else:
                        dictl2[l2[j]]=1
                
        return False
        