class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        nums3=list(set(nums3))
        nums1=nums1+nums2+nums3
        resi=list(set(nums1))
        res=[]
        for i in resi:
            if nums1.count(i)>1:
                res.append(i)
        return res