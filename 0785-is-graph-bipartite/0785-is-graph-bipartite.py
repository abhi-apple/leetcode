# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         col=[-1 for i in range(len(graph))]
#         adj = {}
#         for vertex in range(len(graph)):
#             neighbors = []
#             for neighbor in graph[vertex]:
#                 neighbors.append(neighbor)
#             adj[vertex] = neighbors
        
#         def bfs(ind):
#             que=deque()
#             que.append(ind)
#             col[ind]=1
#             while que:
#                 val=que.popleft()
#                 for i in adj[val]:
#                     if col[i]==-1:
#                         col[i]=1-col[val]
#                         que.append(i)
#                     elif col[i]==col[val]:
#                         return False
            
            
#         for i in range(len(col)):
#             if col[i]==-1:
#                 if not bfs(i):
#                     return False
#         return True
    
from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n

        def bfs(start):
            queue = deque()
            queue.append(start)
            colors[start] = 0

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == -1:
                        colors[neighbor] = 1 - colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False

            return True

        for i in range(n):
            if colors[i] == -1:
                if not bfs(i):
                    return False

        return True
