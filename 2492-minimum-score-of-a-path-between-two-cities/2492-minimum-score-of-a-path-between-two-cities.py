class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj=defaultdict(list)
        for src,dst,di in roads:
            adj[src].append((dst,di))
            adj[dst].append((src,di))
        def dfs(i):
            if i in vis:
                return 
            nonlocal res
            vis.add(i)
            for nei,dis in adj[i]:
                res=min(res,dis)
                dfs(nei)
            
            
        vis=set()
        res=float('inf')
        dfs(1)
        return res