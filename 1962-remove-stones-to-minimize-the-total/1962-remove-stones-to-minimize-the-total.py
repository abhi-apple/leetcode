import heapq   
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles=[-x for x in piles]
        heapq.heapify(piles)

        while k > 0:
            a=heapq.heappop(piles)
            a=a//2
            heapq.heappush(piles,a)
            k-=1

        return -sum(piles)