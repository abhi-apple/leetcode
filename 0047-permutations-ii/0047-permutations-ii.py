class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def f(ind,nums,ans):
            if ind==len(nums):
                if nums not in ans:
                    ans.append(nums.copy())
                return
            for i in range(ind,len(nums)):
                nums[i],nums[ind]=nums[ind],nums[i]
                f(ind+1,nums,ans)
                nums[i],nums[ind]=nums[ind],nums[i]
        f(0,nums,ans)
        return ans