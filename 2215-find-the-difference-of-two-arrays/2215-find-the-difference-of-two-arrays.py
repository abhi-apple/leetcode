class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res=[[],[]]
        for i in nums1:
            if i not in nums2 and i not in res[0]: 
                res[0].append(i)
        for i in nums2:
            if i not in nums1 and i not in res[1]: 
                res[1].append(i)
        return res