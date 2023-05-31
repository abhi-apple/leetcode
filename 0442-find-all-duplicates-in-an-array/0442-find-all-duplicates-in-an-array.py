class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic={}
        res=[]
        for i in nums:
            if i in dic:
                res.append(i)
            else:
                dic[i]=1
        return res
            
            
            
        