class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        adj={i:0 for i in range(n)}
        for i,j in roads:
            adj[i]+=1
            adj[j]+=1
        # print(sorted(adj.values()))
        ans=0
        k=1

        for i in sorted(adj.values()):
            ans+=(i*(k))
            k+=1
            
        return ans