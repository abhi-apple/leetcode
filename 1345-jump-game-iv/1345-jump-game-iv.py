class Solution:
    def minJumps(self, a: List[int]) -> int:
        n = len(a)
        val2id = {}
        for i, x in enumerate(a):
            val2id.setdefault(x, []).append(i)
        d = [inf] * n
        d[0] = 0
        q = [0]
        while len(q) and q[0] != n - 1:
            i = q.pop(0)
            ii = i - 1
            if 0 <= ii and d[ii] is inf:
                d[ii] = d[i] + 1
                q.append(ii)
            ii = i + 1
            if ii < n and d[ii] is inf:
                d[ii] = d[i] + 1
                q.append(ii)
            if a[i] in val2id:
                for ii in val2id[a[i]]:
                    if d[ii] is inf:
                        d[ii] = d[i] + 1
                        q.append(ii)
                del val2id[a[i]]
        return d[n - 1]