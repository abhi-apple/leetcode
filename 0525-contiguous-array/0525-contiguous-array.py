class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
        sums=0
        res=[]
        dic={}
        dic[0]=-1
        
        for i in range(len(nums)):
            sums+=nums[i]
            res.append(sums)
        sums=0
        for i in range(len(res)):
            if res[i] in dic:
                sums=max(sums,i-dic[res[i]])
            else:
                dic[res[i]]=i
        return sums
            
            
                