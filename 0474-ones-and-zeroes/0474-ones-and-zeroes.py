class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        tot=len(strs)
        dp={}
        def rec(i,so,s1):
            if i==tot:
                return 0
            if (i,so,s1) in dp:
                return dp[(i,so,s1)]
            
            now=strs[i]
            cn0,cn1=now.count('0'),now.count('1')
            ntk=rec(i+1,so,s1)
            tk=0
            if so-cn0>=0 and s1-cn1>=0:
                tk=rec(i+1,so-cn0,s1-cn1)+1
            dp[(i,so,s1)]=max(ntk,tk)
            return dp[(i,so,s1)]
        return rec(0,m,n)