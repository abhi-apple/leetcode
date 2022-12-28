class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=1
        mini=1
        res=nums[0]
        for i in nums:
            maxi,mini=max(i,i*maxi,i*mini),min(i,i*maxi,i*mini)
            res=max(res,maxi)
        return res
            