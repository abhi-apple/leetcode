class Solution:
    def findCircleNum(self, isc: List[List[int]]) -> int:
        vis = set()
        adj = {}
        
        for i in range(len(isc)):
            for j in range(len(isc)):
                if i != j and isc[i][j]==1:
                    if i in adj:
                        adj[i].append(j)
                    else:
                        adj[i] = [j]
        # print(adj)
        def dfs(node):
            vis.add(node)
            if node in adj:
                
                for var in adj[node]:
                    if var not in vis:
                        dfs(var)

        cnt = 0
        for i in range(len(isc)):
            if i not in vis:
                dfs(i)
                cnt += 1
        
        return cnt
