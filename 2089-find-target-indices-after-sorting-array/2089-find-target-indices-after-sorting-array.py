class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res=[]
        now=False
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
                now=True
            elif now:
                return res
        return res
            