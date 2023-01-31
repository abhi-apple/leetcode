# class Solution:
#     def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
#         pl = list(zip(ages, scores))
#         pl.sort(key=lambda x: x[0], reverse=True)
#         print(pl)
#         dp=[0]*len(ages)
#         dp[0]=pl[0][1]
#         for i in range(1,len(ages)):
            
#             if pl[i][1]>pl[i-1][1]:
#                 dp[i]=max(dp[i-1],pl[i][1])
#             else:
#                 dp[i]=dp[i-1]+pl[i][1]
            
#         return dp[-1]
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = sorted(zip(ages, scores))
        dp = [0] * n
        for i in range(n):
            dp[i] = players[i][1]
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
        return max(dp)


