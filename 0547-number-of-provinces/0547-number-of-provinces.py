class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # using disjoint set
        n = len(isConnected)
        parent = [i for i in range(n)]
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            pi = find(i)
            pj = find(j)
            
            if pi != pj:
                parent[pj] = pi
                
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]:
                    union(i, j)
        cnt=0
        for i in range(n):
            if parent[i]==i:
                cnt+=1
        return cnt