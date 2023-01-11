import heapq
class Solution:
    def lastStoneWeight(self, st: List[int]) -> int:
        st = [ -x for x in st]
        heapq.heapify(st)
        while len(st)>1:
            a,b=-heappop(st),-heappop(st)
            if a>b:
                heappush(st, b - a)
        return -heappop(st) if len(st) else 0