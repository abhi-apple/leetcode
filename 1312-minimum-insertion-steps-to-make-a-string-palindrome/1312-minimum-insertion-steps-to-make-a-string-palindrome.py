class Solution:
    def minInsertions(self, s: str) -> int:
        t=s[::-1]
        if t==s:
            return 0
        dp={}
        def rec(i,j):
            if i==-1 or j==-1:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i]==t[j]:
                dp[(i,j)]=rec(i-1,j-1)+1
            else:
                dp[(i,j)]=max(rec(i-1,j),rec(i,j-1))
            return dp[(i,j)]
        return len(s)-rec(len(s)-1,len(s)-1)