class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:]=(nums1[:m]+nums2)
        nums1.sort()
        
        # if m==0:
        #     nums1=nums2
        #     return
        # if n==0:
        #     return
        # l=0
        # t=0
        # for i in range(m+n):
        #     if t>=n or (l<m and nums1[l]<nums2[t]):
        #         l+=1
        #     else:
        #         nums1[m+t]=nums1[l]
        #         nums1[l]=nums2[t]
        #         t+=1
        #         l+=1

                