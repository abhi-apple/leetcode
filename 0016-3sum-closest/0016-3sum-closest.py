class Solution:
    def threeSumClosest(self, nums: List[int], t: int) -> int:
        nums.sort()
        cl=float('inf')
        for i in range(len(nums)-2):
            le,ri=i+1,len(nums)-1
            while le<ri:
                sums=nums[le]+nums[ri]+nums[i]
                if abs(sums-t)<abs(cl-t):
                    cl=sums
                elif sums<t:
                    le+=1
                elif sums>t:
                    ri-=1
                else:
                    return cl
        return cl
                    
                    
                    