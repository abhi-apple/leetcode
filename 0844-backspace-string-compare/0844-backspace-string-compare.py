class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res=''
        ret=''
        if s[0]!="#":
            res=s[0]
        if t[0]!="#":
            ret=t[0]
        for i in range(1,len(s)):
            if s[i]=='#':
                res=res[:-1]
                continue
            res=res+s[i]
    
        for i in range(1,len(t)):
            if t[i]=='#':
                ret=ret[:-1]
                continue
            ret=ret+t[i]
         
        if ret==res:
            return True
        return False
        
            