class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def issub(s1,s2):
            i=j=0
            while i<len(s1) and j<len(s2):
                if s1[i]==s2[j]:
                    i+=1
                j+=1
            return len(s1)==i
            
        cach={}
        cnt=0
        for w in words:
            if w not in cach:
                if issub(w,s):
                    cnt+=1
                    cach[w]=True
                else:
                    cach[w]=False
            else:
                if cach[w]:
                    cnt+=1
                    
        return cnt