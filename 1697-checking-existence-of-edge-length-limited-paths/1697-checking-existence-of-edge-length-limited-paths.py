class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]
        def union(v, w):
            parent[find(v)] = find(w)
        edgeList.sort(key = lambda e: e[2])
        queries = sorted(((v,w,limit,i) for i, (v, w, limit) in enumerate(queries)), key = lambda e:e[2])
        parent = [i for i in range(n)]
        j = 0
        res = [0]*len(queries)
        for v,w,limit,i in queries:
            while j < len(edgeList) and edgeList[j][2] < limit:
                p, q, _ = edgeList[j]
                union(p,q)
                j += 1
            res[i] = find(v) == find(w)
        return res
