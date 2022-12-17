class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_indices = {}
        for i, num in enumerate(nums2):
            nums2_indices[num] = i

        # Initialize an empty list to store the results
        results = []

        # For each element in nums1, find its index in nums2 and look for the next greater element
        for num in nums1:
            index = nums2_indices[num]
            found = False
            for j in range(index+1, len(nums2)):
                if nums2[j] > num:
                    results.append(nums2[j])
                    found = True
                    break
            if not found:
                results.append(-1)

        return results
#         arr=[]
#         nu2=len(nums2)
#         for i in range(len(nums1)):
#             k=nums2.index(nums1[i])
#             maxi=nums1[i]
#             print(arr)
#             for j in range(k,nu2):
#                 if maxi<nums2[j]:
#                     arr.append(nums2[j])
#                     break
#                 elif j==nu2-1:
#                     arr.append(-1)
#             # if maxi==nums1[i]:
#             #     arr.append(-1)
            
#         return arr