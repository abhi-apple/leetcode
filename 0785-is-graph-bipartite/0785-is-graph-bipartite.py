class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adj={}
        dic={}
        for i in range(len(graph)):
            adj[i]=[]
            for j in graph[i]:
                adj[i].append(j)
                
        def dfs(node,col):
            if node in dic:
                return dic[node]==col
            dic[node]=col
            for var in adj[node]:
                if not dfs(var,not col):
                    return False
            return True
                
        # return dfs(0,True)
        for i in range(len(graph)):
            if i not in dic:
                if not dfs(i, True):
                    return False
        return True
                    
                    
            