class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        grp=defaultdict(dict)
        for u,v,w in roads:
            grp[u][v]=grp[v][u]=w
        mini=float('inf')
        vist=set()
        que=deque([1])
        while que:
            node=que.popleft()
            for adj,sc in grp[node].items():
                if adj not in vist:
                    que.append(adj)
                    vist.add(adj)
                mini=min(mini,sc)
        return mini