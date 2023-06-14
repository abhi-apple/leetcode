class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        dic={}
        ans=[]
        for i in range(V):
            dic[i]=[]
            for k in adj[i]:
                dic[i].append(k)
        def dfs(node):
            nonlocal ans
            vis.add(node)
            for var in adj[node]:
                if var not in vis:
                    dfs(var)
            ans.append(node)
        vis=set()
        for i in dic:
            if i not in vis:
                dfs(i)
                
            
        return ans[::-1]

        # for 
        # def dfs(node):
        #     vis.add(node)
        #     for var in 
            


#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends