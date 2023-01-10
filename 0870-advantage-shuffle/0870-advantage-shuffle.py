# from collections import Counter
# class Solution:
#     def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         nums1.sort()
#         cnt = Counter(nums1)
#         print(cnt[2])
#         ans=[]
#         ade=0
#         for i in range(len(nums1)):
#             ade=0
#             for j in range(len(nums1)):
#                 if nums1[j]>nums2[i] and cnt[nums1[j]]>=1 :
#                     ans.append(nums1[j])
#                     cnt[nums1[j]]-=1
#                     ade+=1
#                     break
#             if ade==0:
#                 for k in nums1:
#                     if cnt[k]>=1:
#                         ans.append(k)
#                         cnt[k]-=1
#                         break
                    
#         return ans
from collections import Counter
from bisect import bisect_right

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        ans = []
        for num in nums2:
            idx = bisect_right(nums1, num)
            if idx == len(nums1):
                ans.append(nums1[0])
                nums1.pop(0)
            else:
                ans.append(nums1[idx])
                nums1.pop(idx)
        return ans
