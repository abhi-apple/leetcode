class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        ans=sorted(dic, key=lambda x: dic[x])
        ans=ans[::-1]
        return ans[:k]
        # for i in sorted(dic, key=lambda x: dic[x])[::-1]:
        