class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        candyType=set(candyType)
        if len(candyType)>=n//2:
            return n//2
        else:
            return len(candyType)
            