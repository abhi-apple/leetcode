class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp={}
        n=len(nums)
        nums=[1]+nums
        nums.append(1)
        def rec(i,j):
            if i>j:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            maxi=-float('inf')
            
            for k in range(i,j+1):
                val=nums[k]*nums[i-1]*nums[j+1] + rec(i,k-1)+rec(k+1,j)
                maxi=max(val,maxi)
            dp[(i,j)]=maxi
            return dp[(i,j)]
        return rec(1,n)