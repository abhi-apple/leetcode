class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fre={}
        for i in nums:
            if i in fre:
                return i
            else:
                fre[i]=1
        