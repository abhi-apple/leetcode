from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, v: int, adj: List[List[int]]) -> bool:
		#Code here
		vis=[0 for i in range(v)]
		def det(src):
		    vis[src]=1
		    que=[]
		    que.append([src,-1])
		    while que:
		        n,p=que.pop(0)
		        for i in adj[n]:
		            
		            if not vis[i]:
		                
		                vis[i]=1
		                que.append([i,n])
		            elif(p!=i):
		                return True
		    return False
	    for i in range(v):
	        if  vis[i]==0:
	            if det(i)==True:
	                return True
	    return False
		                
		          


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends