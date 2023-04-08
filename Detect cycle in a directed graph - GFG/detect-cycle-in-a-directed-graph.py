#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, v, adj):
        def dfs(node):
            vis[node]=1
            patvis[node]=1
            for i in adj[node]:
                if not vis[i]:
                    if dfs(i):
                        return True
                elif (patvis[i]):
                    return True
            patvis[node]=0
            return False
        # code here
        vis=[0 for i in range(v)]
        patvis=[0 for i in range(v)]
        for i in range(v):
            if not vis[i]:
                if dfs(i):
                    return True
        return False


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