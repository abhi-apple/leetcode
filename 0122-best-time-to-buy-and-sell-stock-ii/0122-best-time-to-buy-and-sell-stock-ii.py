class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                prof+=(prices[i]-prices[i-1])
        return prof