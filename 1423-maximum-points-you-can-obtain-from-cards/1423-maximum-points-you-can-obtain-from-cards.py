class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        sums=sum(nums)
        i=0
        j=len(nums)-k
        maxi=0
        val=sum(nums[:len(nums)-k])
        su=sums-val
        while j<=len(nums):
            maxi=max(maxi,su)
            if j ==len(nums):
                break
            if j<len(nums):
                su-=nums[j]
                su+=nums[i]
                j+=1
                i+=1

        # print(maxi)
        return maxi
            
            
            
            
            
            
            