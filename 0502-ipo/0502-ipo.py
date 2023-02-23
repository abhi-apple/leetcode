class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_heap = []
        profits_heap = []
        for i in range(len(capital)):
            heappush(capital_heap, (capital[i], i))
        available_capital = w
        for i in range(k):

            while capital_heap and capital_heap[0][0] <= available_capital:
                curr_cap, i = heappop(capital_heap)
                heappush(profits_heap, (-profits[i], i))
            

            if not profits_heap:
                break
            available_capital += -heappop(profits_heap)[0]
        return available_capital