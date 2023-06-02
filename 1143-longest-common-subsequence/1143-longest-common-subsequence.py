class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        dp={}
        def rec(i,j):
            if i==-1 or j==-1:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if s1[i]==s2[j]:
                dp[(i,j)]=1+rec(i-1,j-1)
                return dp[(i,j)]
            else:
                tk=rec(i-1,j)
                bt=rec(i,j-1)
                dp[(i,j)]=max(tk,bt)
                return dp[(i,j)]
        return rec(len(s1)-1,len(s2)-1)