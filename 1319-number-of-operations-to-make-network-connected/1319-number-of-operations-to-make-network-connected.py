

class Solution:
    def makeConnected(self, n: int, con: List[List[int]]) -> int:
        par = [i for i in range(n)]
        size = [1 for _ in range(n)]

        def find(node):
            if par[node] == node:
                return node
            par[node] = find(par[node])
            return par[node]

        def union(i, j):
            pi = find(i)
            pj = find(j)
            if size[pi] > size[pj]:
                par[pj] = pi
                size[pi] += size[pj]
            else:
                par[pi] = pj
                size[pj] += size[pi]

        cnt = 0
        for st, ed in con:
            if find(st) != find(ed):
                union(st, ed)
            else:
                cnt += 1

        ans = sum(1 for i in range(n) if par[i] == i) - 1
        if cnt >= ans:
            return ans
        return -1
