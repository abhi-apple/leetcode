class Solution:
    def maxUncrossedLines(self, num1: List[int], num2: List[int]) -> int:
        def rec(i,j):
            if i==len(num1) or j ==len(num2):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            cnt=0
            if num1[i]==num2[j]:
                cnt=1+rec(i+1,j+1)
            else:
                cnt+=max(rec(i+1,j),rec(i,j+1))
            dp[i][j]=cnt
            return cnt
        dp=[[-1 for i in range(len(num2))] for j in range(len(num1))]
        return rec(0,0)