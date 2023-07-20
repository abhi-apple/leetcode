class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp={}
        n=len(s)
        m=len(p)
        def rec(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==n and j==m:
                return True
            if i==n :
                if all(char == "*" for char in p[j:]):
                    return True
                return False
            if j==m:
                return False
            if s[i]==p[j] or p[j]=='?':
                dp[(i,j)]=rec(i+1,j+1)
            elif p[j]=='*':
                dp[(i,j)]=rec(i+1,j+1) or rec(i+1,j) or rec(i,j+1)
            else:
                dp[(i,j)]=False
            return dp[(i,j)]
        return rec(0,0)