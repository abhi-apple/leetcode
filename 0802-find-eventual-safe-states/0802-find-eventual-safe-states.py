class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node):
            vis[node]=1
            patvis[node]=1
            check[node]=0
            for i in (graph[node]):
                if not vis[i]:
                    if dfs(i):
                        check[node]=0
                        return True
                elif patvis[i]:
                    check[node]=0
                    return True
            check[node]=1
            patvis[node]=0
            return False
        v=len(graph)
        vis=[0 for i in range(v)]
        patvis=[0 for i in range(v)]
        check=[0 for i in range(v)]
        safe=[]
        for i in range(v):
            if not vis[i]:
                dfs(i)
        for i in range(v):
            if check[i]==1:
                safe.append(i)
        return safe
