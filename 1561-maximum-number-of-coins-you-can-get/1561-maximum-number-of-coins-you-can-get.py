class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sums=0
        while piles:
            piles.pop()
            sums+=piles.pop()
            piles.pop(0)
        return sums