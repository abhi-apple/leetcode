
import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, v, adj, s):
        #code here
        pq=[(0,s)]
        dist=[float('inf')]*v
        dist[s]=0
        while pq:
            dis,node=heapq.heappop(pq)
            for it in adj[node]:
                nd,le=it[0],it[1]
                if dis+le<dist[nd]:
                    dist[nd]=dis+le
                    heapq.heappush(pq,(dis+le,nd))
        # for i in range(v):
        #     if dist[i]==float('inf'):
                
        return dist


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends