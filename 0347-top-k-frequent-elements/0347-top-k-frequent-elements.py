class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        from heapq import heappush, heappop
        h=[]
        for i in dic:
            heapq.heappush(h,(dic[i],i))
            if len(h)>k:
                heapq.heappop(h)
        res=[]
        for _,i in h:
            res.append(i)
        return res