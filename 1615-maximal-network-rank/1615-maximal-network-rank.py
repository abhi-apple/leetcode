class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj={i:[] for i in range(n)}
        for i,j in roads:
            adj[i].append(j)
            adj[j].append(i)
        deg=[0 for i in range(n)]
        for i in range(n):
            deg[i]=len(adj[i])
        rank=0
        for i in range(n):
            fori=deg[i]
            forj=0
            for j in range(i+1,n):
                now=deg[j]
                if j in adj[i]:
                    now-=1
                forj=max(forj,now)
            rank=max(rank,fori+forj)
                
        return rank
            