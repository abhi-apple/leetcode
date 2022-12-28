import heapq   
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles=[-x for x in piles]
        heapq.heapify(piles)

        while k > 0:
            heapq.heappushpop(piles,piles[0]//2)
            k-=1

        return -sum(piles)