class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False for _ in range(n+1)] for __ in range(m+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[m][n]

# class Solution:
#     def isMatch(self, p: str, s: str) -> bool:
#         dp=[[-1 for i in range(len(p))] for j in range(len(s))]
#         def f(i,j):
#             if i<0 and j<0 :
#                 return True
#             if i<0 and j>=0:
#                 return False
#             if j<0 and i>=0:
#                 return all(x == s[0] for x in s)
#             if dp[i][j]!=-1:
#                 return dp[i][j]
#             if s[i]==p[j] or s[i]=="?":
#                 dp[i][j]=f(i-1,j-1)
#                 return f(i-1,j-1)
#             if s[i]=="*":
#                 dp[i][j]=f(i-1,j) or f(i,j-1)
#                 return f(i-1,j) or f(i,j-1)
#             return False
        
            
#         return f(len(s)-1,len(p)-1)