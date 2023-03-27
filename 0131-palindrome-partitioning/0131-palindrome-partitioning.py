class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        pat=[]
        def ispa(s, st, ed):
            return s[st:ed+1] == s[st:ed+1][::-1]

        def fu(ind,s,pat,res):
            if ind==len(s):
                res.append(pat.copy())
                return
            for i in range(ind,len(s)):
                if ispa(s,ind,i):
                    pat.append(s[ind:i+1])
                    fu(i+1,s,pat,res)
                    pat.pop()
        
                
        fu(0,s,pat,res)
        return res