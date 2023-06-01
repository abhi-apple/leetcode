class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult=1

        if nums.count(0)>1:
            return [0]*len(nums)
        elif nums.count(0)==1:
            ans=[0]*len(nums)
            ind=0
            for i in range(len(nums)):
                if nums[i]==0:
                    ind=i
                else:
                    mult=mult*nums[i]
            ans[ind]=mult
            return ans
        else:
            for i in nums:
                mult=mult*i
            ans=[]
            for i in nums:
                ans.append(mult//i)
            return ans
            