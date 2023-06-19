#User function Template for python3
import heapq

class Solution:
    def spanningTree(self, V, dic):
        vis = set()
        que = []
        heapq.heappush(que, (0, 0))  # Fixed typo: heappush instead of heqppush
        sums = 0  # Initialize sums variable
        while que:
            dis, node = heapq.heappop(que)
            if node in vis:
                continue
            vis.add(node)
            sums += dis  # Fixed typo: add the distance 'dis' to sums
            for var, le in dic[node]:
                if var not in vis:
                    heapq.heappush(que, (le, var))  # Fixed typo: heappush instead of append
        return sums


        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends