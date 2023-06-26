class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def rec(i,arr):
            if i==n:
                res.append(arr)
                return
            rec(i+1,arr)
            rec(i+1,arr+[nums[i]])
            return 
        rec(0,[])
        return res
            
            