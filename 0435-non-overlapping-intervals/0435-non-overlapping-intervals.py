# class Solution:
#     def eraseOverlapIntervals(self, inte: List[List[int]]) -> int:
#         inte.sort(key=lambda x: x[0])
#         dp={}
#         n=len(inte)
#         dp=[[-1 for i in range(n)] for j in range(n)]
#         def rec(i,pr):
#             if i==n:
#                 return 0
#             if dp[i][pr]!=-1:
#                 return dp[i][pr]
#             nt=rec(i+1,pr)
#             tk=0
#             if pr==-1 or inte[i][0]>=inte[pr][1]:
#                 tk=1+rec(i+1,i)
#             dp[i][pr]=max(nt,tk)
#             return dp[i][pr]
#         return n-rec(0,-1)
class Solution:
    def eraseOverlapIntervals(self, inte: List[List[int]]) -> int:
        inte.sort(key=lambda x: x[1])

        n = len(inte)
        if n <= 1:
            return 0

        cnt = 1
        end = inte[0][1]  # Initialize the end with the end time of the first interval
        for i in inte[1:]:
            if i[0]>=end:
                cnt+=1
                end=i[1]
        return n-cnt
