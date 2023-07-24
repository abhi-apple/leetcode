class Solution:
    def wordBreak(self, s: str, wordd: List[str]) -> List[str]:
        dp={}
        res=[]
        wordd=set(wordd)
        n=len(s)
        def rec(i,wrd):
            if i==n:
                res.append(wrd[1:])
                return True
            if (i,wrd) in dp:
                return dp[(i,wrd)]
            dp[(i,wrd)]=False
            for k in range(i,n):
                if s[i:k+1] in wordd and rec(k+1,wrd+' '+s[i:k+1]):
                    dp[(i,wrd)]=True
                    
            
            return dp[(i,wrd)]
        rec(0,'')
        return res
                