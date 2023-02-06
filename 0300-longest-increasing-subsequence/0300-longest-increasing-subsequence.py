# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         def f(ind,pr):
#             if ind==len(nums):
#                 return 0
#             if dp[ind][pr+1]!=-1:
#                 return dp[ind][pr+1]
#             nt=f(ind+1,pr)
#             tk=0
#             if pr==-1 or nums[ind]>nums[pr]:
#                 tk=1+f(ind+1,ind)
#             dp[ind][pr+1]=max(nt,tk)
#             return dp[ind][pr+1]
        
#         dp=[[-1 for i in range(len(nums)+1)] for j in range(len(nums))]
#         return f(0,-1)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0
