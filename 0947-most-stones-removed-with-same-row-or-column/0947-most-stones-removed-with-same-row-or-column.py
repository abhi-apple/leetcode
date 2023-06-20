class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        maxr = 0
        maxc = 0
        
        def find(node):
            if par[node] == node:
                return node
            return find(par[node])
        
        def union(i, j):
            pi = find(i)
            pj = find(j)
            if pi!=pj:
                
                if size[pi] > size[pj]:
                    par[pj] = pi
                    size[pi] += size[pj]
                else:
                    par[pi] = pj
                    size[pj] += size[pi]
            
        
        for i, j in stones:
            maxr = max(maxr, i)
            maxc = max(maxc, j)
        
        n = maxr + maxc + 2  
        
        par = [i for i in range(n)]
        size = [1] * (n)
        for i, j in stones:
            pi = i
            pj = j + maxr + 1
            
            union(pi, pj)
        
        cnt = 0
        for i in range(n):
            if par[i] == i and size[i] > 1:
                cnt += 1
        
        return len(stones)-cnt

                
            