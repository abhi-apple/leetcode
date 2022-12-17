class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        nu2=len(nums2)
        for i in range(len(nums1)):
            k=nums2.index(nums1[i])
            maxi=nums1[i]
            print(arr)
            for j in range(k,nu2):
                if maxi<nums2[j]:
                    arr.append(nums2[j])
                    break
                elif j==nu2-1:
                    arr.append(-1)
            # if maxi==nums1[i]:
            #     arr.append(-1)
            
        return arr