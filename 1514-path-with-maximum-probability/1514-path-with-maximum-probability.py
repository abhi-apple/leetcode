from typing import List
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], scc: List[float], start: int, end: int) -> float:
        adj = {i: [] for i in range(n)}
        for i in range(len(edges)):
            st, ed = edges[i]
            prb = scc[i]
            adj[st].append((ed, prb))
            adj[ed].append((st, prb))
        sq = [(-1, start)]
        seen = set()
        while sq:
            wei, v = heapq.heappop(sq)
            if v == end:
                return -wei
            seen.add(v)
            for nei, neiw in adj[v]:
                if nei not in seen:
                    heapq.heappush(sq, (neiw * wei, nei))
        return 0.0

                