class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        jumps = [0]*(n+1)
        for i in range(n+1):
            l, r = max(0,i-ranges[i]),  min(n,i+ranges[i])
            jumps[l] = max(jumps[l],r-l)
        step = start = end = 0
        while end < n:
            start, end = end+1, max(i+jumps[i] for i in range(start, end+1))
            if start > end:
                return -1
            step += 1
        return step