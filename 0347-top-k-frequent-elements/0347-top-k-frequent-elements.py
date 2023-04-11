class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    
        ans=[sorted_dic[i][0] for i in range(k)]
        return ans
