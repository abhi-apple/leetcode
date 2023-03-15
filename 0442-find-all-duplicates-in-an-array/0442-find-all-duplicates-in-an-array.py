class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic={}
        res=[]
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
                res.append(nums[i])
            else:
                dic[nums[i]]=1
        return res
        