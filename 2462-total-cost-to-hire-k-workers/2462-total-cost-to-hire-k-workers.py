import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, cand: int) -> int:
        pq1=[]
        pq2=[]
        ans=0
        cnt=0
        i=0
        j=len(costs)-1
        while cnt<k:
            while len(pq1)<cand and i<=j:
                heapq.heappush(pq1,costs[i])
                i+=1
            while len(pq2)<cand and j>=i:
                heapq.heappush(pq2,costs[j])
                j-=1
            a=pq1[0] if len(pq1)>0 else float('inf')
            b=pq2[0] if len(pq2)>0 else float('inf')
            if a<=b:
                ans+=a
                heapq.heappop(pq1)
            else:
                ans+=b
                heapq.heappop(pq2)
            cnt+=1
        return ans