class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        dp=[[-1 for i in range(len(w2))] for j in range(len(w1))]
        def f(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if dp[i][j]!=-1:
                return dp[i][j]
            if w1[i]==w2[j]:
                dp[i][j]=f(i-1,j-1)
                return f(i-1,j-1)
            else:
                dp[i][j]=1+min(f(i,j-1),f(i-1,j),f(i-1,j-1))
                return 1+min(f(i,j-1),f(i-1,j),f(i-1,j-1))
            
            
        return f(len(w1)-1,len(w2)-1)
        