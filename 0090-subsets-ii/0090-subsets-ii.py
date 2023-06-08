
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        nums.sort()
        fin=[]
        def rec(i,arr):
            if i==n:
                if arr not in fin:
                    fin.append(arr)
                return 
            rec(i+1,arr)
            rec(i+1,arr+[nums[i]])
            return 
        rec(0,[])
        return fin