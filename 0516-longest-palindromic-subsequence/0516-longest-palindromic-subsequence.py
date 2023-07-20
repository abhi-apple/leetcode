class Solution:
    def longestPalindromeSubseq(self, s1: str) -> int:
        s2=s1[::-1]
        dp={}
        n=len(s1)
        def rec(i,j):
            if i==n or j==n:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if s1[i]==s2[j]:
                dp[(i,j)]=rec(i+1,j+1)+1
            else:
                dp[(i,j)]=max(rec(i+1,j),rec(i,j+1))
            return dp[(i,j)]
        return rec(0,0)