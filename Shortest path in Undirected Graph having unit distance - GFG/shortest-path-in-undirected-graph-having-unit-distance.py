#User function Template for python3
from collections import deque
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        adj={i:[] for i in range(n)}
        
        for st,ed in edges:
            adj[st].append(ed)
            adj[ed].append(st)
        dis=[float('inf')]*n
        dis[src]=0
        que=deque([src])
        vis=set()
        while que:
            var=que.popleft()
            for v in adj[var]:
                if dis[var]+1<dis[v]:
                    dis[v]=dis[var]+1
                    que.append(v)
        for i in range(n):
            if dis[i]==float('inf'):
                dis[i]=-1
        return dis
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends