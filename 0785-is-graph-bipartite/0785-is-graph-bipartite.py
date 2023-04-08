class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(nd):
            
            
            que.append(nd)
            
            col[nd]=0
            while que:
                node=que.pop(0)
                for i in graph[node]:
                    if col[i]==-1:
                        col[i]=not col[node]
                        que.append(i)
                    elif col[i]==col[node]:
                        return False
            return True
                
        col=[-1 for i in range(len(graph))] 
        que=[]
        for i in range(len(graph)):
            if col[i]==-1:
                if not bfs(i):
                    return False
        return True
    
    
