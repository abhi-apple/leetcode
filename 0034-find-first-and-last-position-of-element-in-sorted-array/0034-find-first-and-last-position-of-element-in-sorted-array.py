class Solution:
    def searchRange(self, nums: List[int], tar: int) -> List[int]:
        st=False
        res=[-1,-1]
        for i in range(len(nums)):
            if not st and nums[i]==tar:
                res[0]=i
                st=True
            if nums[i]==tar:
                res[1]=i

        return res