class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def f(ind,nums,ans):
            if ind==len(nums):
                ans.append(nums.copy())
                # ds=nums.copy()
                # if ds not in ans:
                #     ans.append(ds)
                return
            for i in range(ind,len(nums)):
                nums[i],nums[ind]=nums[ind],nums[i]
                f(ind+1,nums,ans)
                nums[i],nums[ind]=nums[ind],nums[i]
        f(0,nums,ans)
        return ans