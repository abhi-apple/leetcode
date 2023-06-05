class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp={}
        def rec(i,pr):
            if i==len(nums):
                return []
            if (i,pr) in dp:
                return dp[(i,pr)]
            nt=rec(i+1,pr)
            tk=[]
            if pr==-1 or nums[i] % nums[pr]==0 :
                tk=[nums[i]]+rec(i+1,i)
            dp[(i,pr)]=max(nt,tk,key=len)
            return dp[(i,pr)]
        return rec(0,-1)
            