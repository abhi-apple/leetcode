class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ar1=s1.split(' ')
        ar2=s2.split(' ')
        rea=[]
        fr1={}
        for i in ar1+ar2:
            if i in fr1:
                fr1[i]+=1
            else:
                fr1[i]=1
        for i in ar1+ar2:
            if fr1[i]==1:
                rea.append(i)
        return rea
        