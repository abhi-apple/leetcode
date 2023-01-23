class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        fin=[]
        for i in range(2**(len(nums))):
            ar=[]
            for j in range(len(nums)):
                if i & (1<<j):
                    ar.append(nums[j])
            ar.sort()
            if ar not in fin:
                fin.append(ar)
        return fin