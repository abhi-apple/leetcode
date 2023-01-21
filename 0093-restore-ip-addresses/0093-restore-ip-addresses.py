class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        if len(s)>12:
            return res
        def bac(i,dot,cur):
            if dot==4 and  i==len(s):
                res.append(cur[:-1])
            if dot>4:
                return 
            for j in range(i,min(i+3,len(s))):
                if int(s[i:j+1])<256 and (i==j or s[i]!='0'):
                    bac(j+1,dot+1,cur+s[i:j+1]+'.')
        bac(0,0,'')
        return res
                