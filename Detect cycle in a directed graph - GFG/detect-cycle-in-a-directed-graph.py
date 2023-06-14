#User function Template for python3


# class Solution:
    
#     #Function to detect cycle in a directed graph.
#     def isCyclic(self, V, adj):
#         def dfs(node):
#             nonlocal vis
#             if  node in vis:
#                 return True
#             for var in adj[node]:
#                 if var not in vis:
#                     vis.add(var)
#                     if dfs(var):
#                         return True
#                 else:
#                     return True
#             return False
#         for k in adj:
#             vis=set()
#             if dfs(k):
#                 return True
#         return False


        

from collections import deque

class Solution:
    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        indegree = [0] * V
        for i in range(V):
            for k in adj[i]:
                indegree[k] += 1
        
        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        
        cnt = 0
        while queue:
            node = queue.popleft()
            cnt += 1
            
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if cnt == V:
            return False
        return True






#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends