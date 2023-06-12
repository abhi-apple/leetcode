class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        
        be = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                res.append(str(be) if be == nums[i - 1] else str(be) + "->" + str(nums[i - 1]))
                be = nums[i]
        
        res.append(str(be) if be == nums[-1] else str(be) + "->" + str(nums[-1]))
        
        return res
