class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
      
        res=[]
        for i in nums:
            if dic[i]>len(nums)/3 and i not in res:
                res.append(i)
        return res
            