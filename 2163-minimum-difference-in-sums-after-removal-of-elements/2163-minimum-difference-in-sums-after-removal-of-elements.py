class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n=len(nums)//3
        lft=[-x for x in nums[:n]]
        heapify(lft)
        sumlf=[sum(nums[:n])]
        for i in range(n,2*n):
            cur=heappushpop(lft,-nums[i])
            sumlf.append(sumlf[-1]+cur+nums[i])
        rgt=nums[2*n:]
        heapify(rgt)
        sumrg=[sum(nums[2*n:])]
        for i in reversed(range(n,2*n)):
            cur=heappushpop(rgt,nums[i])
            sumrg.append(sumrg[-1]-cur+nums[i])
        sumrg=sumrg[::-1]
        ans=float('inf')
        for a,b in zip(sumlf,sumrg):
            ans=min(ans,a-b)
        return ans
    
            
#         N = len(nums) // 3
        
#         left = [-n for n in nums[:N]]
#         heapify(left)
#         sum_left = [sum(nums[:N])]
        
#         for i in range(N, 2*N):
#             curr = heappushpop(left, -nums[i])
#             sum_left.append(sum_left[-1] + curr + nums[i])
            
#         right = nums[2*N:]
#         heapify(right)
#         sum_right = [sum(right)]
        
#         for i in reversed(range(N, 2*N)):
#             curr = heappushpop(right, nums[i])
#             sum_right.append(sum_right[-1] - curr + nums[i])
            
#         return min(l - r for l, r in zip(sum_left, sum_right[::-1]))