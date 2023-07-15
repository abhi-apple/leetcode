# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         adj={}
#         for i in range(len(graph)):
#             adj[i]=[]
#             for k in graph[i]:
#                 adj[i].append(k)
#         stack=deque()
#         coladj={}
#         def rec(i,colad):
#             print(i,colad)
#             stack.append((i,colad))
#             while stack:
#                 node,col=stack.popleft()
#                 coladj[node]=col
#                 for var in adj[node]:
#                     if var not in coladj:
#                         stack.append((var,not col))
#                     else:
#                         if coladj[var]==col:
#                             return False
#         for i in range(len(graph)):
#             if i not in coladj:
#                 rec(i,True)
                
#         return True

from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        coladj = {}
        
        def dfs(node, col):
            if node in coladj:
                return coladj[node] == col
            
            coladj[node] = col
            for neighbor in graph[node]:
                if not dfs(neighbor, not col):
                    return False
            return True

        for i in range(len(graph)):
            if i not in coladj:
                if not dfs(i, True):
                    return False

        return True

                
                
                