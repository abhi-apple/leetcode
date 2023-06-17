class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        adj={i:[] for i in range(n)}
        ind=[0]*n
        for i in range(n):
            for k in graph[i]:
                adj[k].append(i)
                ind[i]+=1
        que=deque()
        for i in range(n):
            if ind[i]==0:
                que.append(i)
        res=[]
        while que:
            var=que.popleft()
            res.append(var)
            for va in adj[var]:
                ind[va]-=1
                if ind[va]==0:
                    que.append(va)
        return sorted(res)