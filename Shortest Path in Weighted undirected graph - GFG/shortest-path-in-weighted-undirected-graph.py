#User function Template for python3
import heapq

class Solution:
    def shortestPath(self, n, m, edges):
        adj = {i: [] for i in range(n + 1)}  # Include node 0 in the dictionary
        for st, ed, dis in edges:
            adj[st].append((ed, dis))
            adj[ed].append((st, dis))

        st = [(0, 1, [])]  # Using (dis, node, path) format in the heap
        dis = [float('inf')] * (n + 1)
        dis[1] = 0

        while st:
            let, node, ar = heapq.heappop(st)
            if node == n:
                return ar + [n]
            for var, le in adj[node]:
                if let + le < dis[var]:
                    dis[var] = let + le
                    heapq.heappush(st, (let + le, var, ar + [node]))

        return [-1]


            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        edges = []
        for i in range(m):
            node1, node2, weight = list(map(int, input().split()))
            edges.append([node1, node2, weight])
        obj = Solution()
        ans = obj.shortestPath(n, m, edges)
        for e in ans:
            print(e, end = ' ')
        print()
# } Driver Code Ends