class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indeg=[0 for i in range(len(graph))]
        
        stack=deque()
        for i in range(len(indeg)):
            indeg[i]=len(graph[i])
            if indeg[i]==0:
                stack.append(i)
        adj=[[] for i in range(len(graph))]
        for i in range(len(graph)):
            for j in graph[i]:
                adj[j].append(i)
        # print(adj)
        ans=[]
        while stack:
            node=stack.popleft()
            ans.append(node)
            for var in adj[node]:
                indeg[var]-=1
                if indeg[var]==0:
                    stack.append(var)
        ans.sort()
        return ans
            
                