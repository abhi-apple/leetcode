class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        low = 0
        high = m
        medianPos = (m+n+1)//2
        while low <= high:
            cut1 = (low+high)//2
            cut2 = medianPos - cut1


            l1 = float('-inf') if cut1 == 0 else nums1[cut1-1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2-1]
            r1 = float('inf') if cut1 == m else nums1[cut1]
            r2 = float('inf') if cut2 == n else nums2[cut2]


            if l1 <= r2 and l2 <= r1:
                if (m+n) % 2 != 0:
                    return max(l1, l2)
                else:
                    return (max(l1, l2)+min(r1, r2))/2.0
            elif l1 > r2:
                high = cut1-1
            else:
                low = cut1+1
        return 0.0


#         if len(nums1) > len(nums2):
#             return self.findMedianSortedArrays(nums2, nums1)  # Add 'return' here
#         n1 = len(nums1)
#         n2 = len(nums2)
#         low = 0
#         high = n1
#         sums = (n1 + n2 + 1) // 2  # Use integer division operator '//' instead of '>>'
#         while low <= high:
#             cut1 = (low + high) // 2
#             cut2 = sums - cut1
#             left1 = float('-inf')
#             left2 = float('-inf')
#             if cut1 != 0:
#                 left1 = nums1[cut1 - 1]
#             if cut2 != 0:
#                 left2 = nums2[cut2 - 1]
#             right1 = float('inf')
#             right2 = float('inf')
#             if cut1 != n1:
#                 right1 = nums1[cut1]  # Use 'right1' here instead of 'left1'
#             if cut2 != n2:
#                 right2 = nums2[cut2]  # Use 'right2' here instead of 'left2'

#             if left1 <= right2 and left2 <= right1:
#                 if (n1 + n2) % 2 == 1:  # Use modulus operator '%' instead of '&' for odd/even check
#                     return (max(left1, left2) + min(right1, right2)) / 2
#                 else:
#                     return (max(left1, left2))  # Use 'max' instead of 'left2' here
#             elif left1 > right2:
#                 high = cut1 - 1  # Change 'cnt1' to 'cut1' here
#             else:
#                 low = cut1 + 1  # Change 'cnt1' to 'cut1' here
#         return 0.0
