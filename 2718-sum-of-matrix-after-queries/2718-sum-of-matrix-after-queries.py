from typing import List

class Solution:
    def matrixSumQueries(self, n: int, ar: List[List[int]]) -> int:
        ar = ar[::-1]
        r = 0
        c = 0
        sums = 0
        mr = {}
        mc = {}
        for i in ar:
            tp = i[0]
            ind = i[1]
            val = i[2]
            if tp == 1 and (ind not in mc or mc[ind] != 1):
                sums += (val * max(n - r, 0))
                mc[ind] = 1
                c += 1
            elif tp == 0 and (ind not in mr or mr[ind] != 1):
                sums += (val * max(n - c, 0))
                mr[ind] = 1
                r += 1
        return sums
