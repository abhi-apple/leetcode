class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        # def f(i1,i2):
        #     if i1<0 or i2<0:
        #         return 0
        #     if dp[i1][i2]!=-1:
        #         return dp[i1][i2]
        #     if s1[i1]==s2[i2]:
        #         dp[i1][i2]=1+f(i1-1,i2-1)
        #         return 1+f(i1-1,i2-1)
        #     else:
        #         dp[i1][i2]=max(f(i1-1,i2),f(i1,i2-1))
        #         return max(f(i1-1,i2),f(i1,i2-1))
        dp=[[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        for i in range(len(s1)+1):
            dp[i][0]=0
        for j in range(len(s2)+1):
            dp[0][j]=0
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[len(s1)][len(s2)]