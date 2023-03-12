class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        cnt=len(nums)/3
        nums=set(nums)
        res=[]
        for i in nums:
            if dic[i]>cnt:
                res.append(i)
        return res
            