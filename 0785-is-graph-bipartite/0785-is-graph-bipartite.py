class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        col=[-1]*n
        
        def bfs(ind):
            que=deque()
            que.append(ind)
            col[ind]=1
            while que:
                print(col)
                val=que.popleft()
            
                for i in graph[val]:
                    if col[i]==-1:
                        col[i]= not col[val]
                        que.append(i)
                    elif col[i]==col[val]:
                        print(i,val)
                        return False
            return True
            
        for i in range(len(col)):
            if col[i]==-1:
                if not bfs(i):
                    print(i)
                    return False
        return True
    
