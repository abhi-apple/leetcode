class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=len(nums1)
        n2=len(nums2)
        ans=[]
        if n1>n2:
            for i in nums2:
                if i in nums1:
                    if i not in ans:
                        ans.append(i)
        else:
            for i in nums1:
                if i in nums2:
                    if i not in ans:
                        ans.append(i)
        return ans