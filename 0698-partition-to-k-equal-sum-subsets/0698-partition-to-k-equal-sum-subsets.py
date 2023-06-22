# from typing import List

# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         tot = sum(nums)
#         if tot % k != 0:
#             return False
#         tars = tot // k
#         usd=[False]*len(nums)
#         def rec(i,cnt,sums):
#             if cnt==0:
#                 return True
#             if sums==tars:
#                 return rec(0,cnt-1,0)
#             # print(i,cnt,sums)
#             for j in range(i,len(nums)):
#                 if usd[i] and sums+nums[j]>tars:
#                     continue
#                 usd[j]=True
#                 if rec(j+1,cnt,sums+nums[j]): return True
#                 usd[j]=False
#             return False
#         rec(0,k,0)
# from typing import List

# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         total_sum = sum(nums)
#         if total_sum % k != 0:
#             return False
#         target_sum = total_sum // k
#         used = [False] * len(nums)
#         dp={}
#         nums.sort()
#         def rec(i, count, current_sum):
#             if count == 0:
#                 return True
#             if current_sum == target_sum:
#                 return rec(0, count - 1, 0)

#             for j in range(i, len(nums)):
#                 if i>0 and not used and nums[i]==nums[i-1]:
#                     continue
#                 if used[j] or current_sum + nums[j] > target_sum:
#                     continue
#                 used[j] = True
#                 if rec(j + 1, count, current_sum + nums[j]):
#                     return True
#                 used[j] = False

#             return False

#         return rec(0, k, 0)

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

            n = len(nums)
            nums.sort(reverse=True)
            total = sum(nums)
            if total % k != 0:
                return False

            target = int(total / k)
            used = [False] * n

            def dfs(index, total, k): 

                if k == 0:
                    return True

                if total == 0:
                    return dfs(0, target, k - 1)

                for i in range(index, n):

                    if i > 0 and not used[i - 1] and nums[i] == nums[i - 1]:
                        continue

                    if used[i] or total - nums[i] < 0:
                        continue

                    used[i] = True
                    if dfs(i + 1, total - nums[i], k):
                        return True
                    used[i] = False
                return False

            return dfs(0, target, k)


                

