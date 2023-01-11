class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        ans=[]
        for i in nums:
            if dic[i]==1:
                ans.append(i)
        return ans