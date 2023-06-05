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
        inte.sort(key=lambda x: x[0])

        n = len(inte)
        if n <= 1:
            return 0

        count = 0
        end = inte[0][1]  # Initialize the end with the end time of the first interval

        for i in range(1, n):
            if inte[i][0] < end:  # Overlapping interval found
                count += 1
                end = min(end, inte[i][1])  # Update the end time to the minimum of the current and previous interval
            else:
                end = inte[i][1]  # No overlap, update the end time with the current interval

        return count
