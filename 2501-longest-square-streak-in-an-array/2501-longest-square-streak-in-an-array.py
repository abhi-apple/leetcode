class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        maxi=0
        j=0
        cnt=Counter(nums)
        vis=set()
        while i<len(nums):
            le=0
            val=nums[i]
            
            while val in cnt and val not in vis:
                vis.add(val)
                le+=1
                val=val*val
            i+=1
            maxi=max(maxi,le)
        if maxi>1:
            return maxi
        return -1
            
                
            