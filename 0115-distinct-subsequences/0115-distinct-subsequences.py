class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        dp={}
        def rec(i,j):
            if (i,j) in dp:
                return dp[(i,j)]

            if j==m:
                return 1
            if i==n:
                return 0
            if s[i]==t[j]:
                dp[(i,j)]=rec(i+1,j+1)+rec(i+1,j)
            else:
                dp[(i,j)]=rec(i+1,j)
            return dp[(i,j)]
        return rec(0,0)
            