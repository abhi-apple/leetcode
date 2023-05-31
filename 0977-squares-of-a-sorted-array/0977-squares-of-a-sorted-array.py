class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        res=[0]*(j+1)
        ind=j
        while i<=j:
            if nums[i]*nums[i]<nums[j]*nums[j]:
                res[ind]=nums[j]*nums[j]
                j-=1
            else:
                res[ind]=nums[i]*nums[i]
                i+=1
            ind-=1
        return res
        