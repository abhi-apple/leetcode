class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans=[False for i in range(len(nums)+1)]
        for i in range(len(nums)):
            if ans[nums[i]]:
                return nums[i]
            ans[nums[i]]=True