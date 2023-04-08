class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(nd,co):
            col[nd] = co
            for i in graph[nd]:
                if col[i] == -1:
                    if not dfs(i,1-co):
                        return False
                elif col[i] == co:
                    return False
            return True
                
        col=[-1 for i in range(len(graph))] 
        for i in range(len(graph)):
            if col[i]==-1:
                if not dfs(i,0):
                    return False
        return True

    
    
