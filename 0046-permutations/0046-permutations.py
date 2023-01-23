class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        ds=[]
        fre=[False for i in range(len(nums))]
        def f(ds,fre,ans):
            if len(ds)==len(nums):
                ans.append(ds.copy())
                return 
            for i in range(len(nums)):
                if not fre[i]:
                    fre[i]=True
                    ds.append(nums[i])
                    f(ds,fre,ans)
                    ds.pop()
                    fre[i]=False
        f(ds,fre,ans)
        return ans