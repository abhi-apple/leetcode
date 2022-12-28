class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt=0
        st=0
        end=0
        pd=1
        while end<len(nums):
            pd*=nums[end]
            while pd>=k and st<=end:
                pd/=nums[st]
                st+=1
            cnt+=end-st+1
            end+=1
        return cnt
            