from collections import deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for st, des, pr in flights:
            adj[st].append([des, pr])
        
        dis = [float('inf')] * n
        dis[src] = 0
        
        que = []
        heapq.heappush(que,(0, src, 0))
        
        while que:
            inte, cur, distance = heapq.heappop(que)
            if inte > k:
                continue
            for nxt, val in adj[cur]:
                if inte  <= k  and dis[nxt]>distance + val:
                    dis[nxt] =  distance + val
                    heapq.heappush(que,(inte + 1, nxt, dis[nxt]))
        
        if dis[dst] == float('inf'):
            return -1
        
        return dis[dst]
