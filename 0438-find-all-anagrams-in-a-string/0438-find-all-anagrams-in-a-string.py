class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lis=list(p)
        lis.sort()
        sl=list(s)
        i=0
        j=len(lis)
        fin=[]
        while j<=len(sl):
            ans=sl[i:j]
            ans.sort()
            if lis==ans:
                fin.append(i)
            i+=1
            j+=1
            
        return fin