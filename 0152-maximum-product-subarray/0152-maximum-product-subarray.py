class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=-float('inf')
        if n==1:
            return nums[0]
        @cache
        def rec(i,prod):
            nonlocal maxi
            if i==n:
                maxi=max(maxi,prod)
                return prod
            
            pk=rec(i+1,prod*nums[i])
            maxi=max(maxi,prod)
            return pk
        for i in range(n):
            rec(i+1,nums[i])
        
        return maxi