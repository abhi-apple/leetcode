class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,time in times:
            adj[u].append([v,time])
        dist=[float('inf') for i in range(n)]
        stack=[]
        dist[k-1]=0
        heapq.heappush(stack,(0,k))
        while stack:
            time,node=heapq.heappop(stack)
            for pat,vali in adj[node]:
                if dist[pat-1]>time+vali:
                    dist[pat-1]=time+vali
                    heapq.heappush(stack,(dist[pat-1],pat))
        if  any(x == float('inf') for x in dist):
            return -1
        return max(dist)
                