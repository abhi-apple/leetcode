# class Solution:
#     def numSquares(self, n: int) -> int:
#         nums=[]
#         val=1
#         while val*val<=10**4:
#             nums.append(val*val)
#             val+=1
#         dp={}
#         def rec(i,value):
#             if value==0:
#                 return 0
#             if value<0 or i<=-1:
#                 return float('inf')
#             dp[(i,value)]=float('inf')
#             if value-nums[i]>=0:
#                 dp[(i,value)]=min(rec(i,value-nums[i])+1,dp[(i,value)])
#             dp[(i,value)]=min(dp[(i,value)],rec(i-1,value))
#             return dp[(i,value)]
#         return rec(len(nums)-1,n)


class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        val = 1
        while val * val <= 10 ** 4:
            nums.append(val * val)
            val += 1

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] = min(dp[i], dp[i - num] + 1)

        return dp[n]
