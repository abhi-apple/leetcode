# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         dp={}
#         cnt=0
#         n=len(nums)
#         def rec(i,arr,sums):
            
#             nonlocal cnt
#             if sums==target:
#                 cnt+=1
#                 return True
#             if (i,tuple(arr)) in dp:
#                 return dp[(i,tuple(arr))]
#             for k in range(n):
#                 if sums+nums[k]<=target:
#                     rec(k,arr+[nums[k]],sums+nums[k])
#             dp[(i,tuple(arr))]=True
#             return True
#         rec(0,[],0)
#         return cnt 

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # There is one way to make a sum of 0 (by choosing nothing).

        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]
