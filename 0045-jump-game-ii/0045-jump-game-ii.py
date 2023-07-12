class Solution:
    def jump(self, nums: List[int]) -> int:
        l=r=0
        maxi=0
        while r<len(nums)-1:
            maxre=0
            for i in range(l,r+1):
                maxre=max(maxre,nums[i]+i)
            maxi+=1
            l=r+1
            r=maxre
        return maxi
            
                