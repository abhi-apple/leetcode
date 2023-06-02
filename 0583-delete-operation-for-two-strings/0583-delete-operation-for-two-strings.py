class Solution:
    def minDistance(self, s: str, r: str) -> int:
        dp={}
        def rec(i,j):
            if i==-1 or j==-1:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i]==r[j]:
                dp[(i,j)]=rec(i-1,j-1)+1
            else:
                dp[(i,j)]=max(rec(i-1,j),rec(i,j-1))
            return dp[(i,j)]
        ans=rec(len(s)-1,len(r)-1)
        return (len(s)-ans)+(len(r)-ans)