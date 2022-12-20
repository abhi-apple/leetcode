class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        for i in range(len(nums)):
            if nums[i] & 1==1:
                odd.append(nums[i])
            if nums[i] & 1!=1:
                even.append(nums[i])
        even.extend(odd)
        return even
        # ans=[]
        # cp=nums.copy()
        # for i in range(len(cp)):
        #     if cp[i] & 1==1:
        #         nums.remove(cp[i])
        #         ans.append(cp[i])
        # print(ans)
        # nums.extend(ans)
        # return nums