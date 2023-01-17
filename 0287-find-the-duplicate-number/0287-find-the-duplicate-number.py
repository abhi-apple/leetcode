class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        prev=-10000
        for i in nums:
            if prev==i:
                return i
            prev=i