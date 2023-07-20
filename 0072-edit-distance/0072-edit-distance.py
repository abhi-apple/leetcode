class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp={}
        n=len(word1)
        m=len(word2)
        def rec(i,j):
            if i==n and j==m:
                return 0
            if i==n:
                return m-j
            if j==m:
                return n-i
            if (i,j) in dp:
                return dp[(i,j)]
            if word1[i]==word2[j]:
                dp[(i,j)]=rec(i+1,j+1)
            else:
                dp[(i,j)]=min(rec(i+1,j+1),rec(i+1,j),rec(i,j+1))+1
            return dp[(i,j)]
        return rec(0,0)
                